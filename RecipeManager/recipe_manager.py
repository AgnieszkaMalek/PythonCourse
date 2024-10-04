# recipe_manager.py

import os.path
import json
from typing import Dict, List
from pprint import pprint

# local libs
import recipe_module as rm

DATA_FILE = 'Data/list_of_burgers.json'  # Path to the JSON file with recipes
valid_file = True
burger_stack = ("BurgerName", "TypeOfMeat", "VeggieBurger", "BurgerToppings", "BurgerSauce")
list_of_burgers = list()


# Function to pause program and wait for user to press Enter key
def pause_app() -> None:
    print("Press Enter to continue.")
    input()


# Function to check if the JSON file exists
def file_check(file_name) -> bool:
    is_file_exists = os.path.exists(file_name)
    if not is_file_exists:
        print("The data file does not exist.")
    return is_file_exists


# Function to read and validate JSON file
def load_data_file(data_file: str) -> list:
    valid_file = True
    if file_check(data_file):
        valid_file = True
        with open(data_file, mode="r", encoding="utf-8") as read_file:
            try:
                burger_data = json.load(read_file)
                for burger in burger_data['burgers']:
                    for k in burger.keys():
                        if k not in burger_stack:
                            valid_file = False
                            print("JSON file includes invalid data")
                            break
                if len(burger_data['burgers']) == 0:
                    print("No burgers in data file")
                    valid_file = False
            except json.decoder.JSONDecodeError:
                print("JSON file error - Invalid data structure")
                valid_file = False
    if valid_file:
        for burger in burger_data['burgers']:
            for k, v in burger.items():
                match k:
                    case "BurgerName":
                        list_of_burgers.append(rm.Burger(name=v))
                    case "TypeOfMeat":
                        list_of_burgers[-1].meat = v
                    case "VeggieBurger":
                        list_of_burgers[-1].veggie = v
                    case "BurgerToppings":
                        list_of_burgers[-1].toppings = v
                    case "BurgerSauce":
                        list_of_burgers[-1].sauce = v
    return list_of_burgers


# Function to save data to JSON file
def save_data(burger_list) -> None:
    json_list = []
    for burger in burger_list:
        json_list.append({burger_stack[0]: burger.name,
                         burger_stack[1]: burger.meat,
                         burger_stack[2]: burger.veggie,
                         burger_stack[3]: burger.toppings,
                         burger_stack[4]: burger.sauce})

    json_dict = {"burgers": json_list}
    with open(DATA_FILE, "w") as write_file:
        json.dump(json_dict, write_file, indent=4)


# Function to add new Burger
def add_new_burger(burger_list) -> None:
    burger_name = input("Enter Burger name: ")
    burger_list.append(rm.Burger(name=burger_name))
    burger_meat = input("Enter Burger meat: ")
    burger_list[-1].meat = burger_meat
    burger_toppings = input("Enter Burger toppings (separated by comma): ")
    burger_list[-1].toppings = burger_toppings.split(",")
    burger_sauce = input("Enter Burger sauce: ")
    burger_list[-1].sauce = burger_sauce
    if len(burger_meat) == 0:
        burger_list[-1].veggie = True
    save_data(burger_list)
    print(f"\nNew Burger \"{burger_name}\" added to the list.")
    pause_app()


# Function to change Burger details
def edit_burger(burger_list) -> None:
    if not burger_list:
        print("\nNo Burges found.")
        pause_app()
        return
    print("\nList of Burgers: ")
    temp_list = []
    qty_of_burgers = 0
    for i, burger in enumerate(burger_list, start=1):
        temp_list.append(burger.name)
        print(f"\t{i}. {burger.name}")
        qty_of_burgers += 1

    chosen_burger = input(f"\nWhich Burger would you like to edit? Enter you choice (1-{qty_of_burgers}):")
    if not chosen_burger.isnumeric() or int(chosen_burger) > qty_of_burgers:
        print("Invalid choice!")
    else:
        i = int(chosen_burger)
        i -= 1
        for burger in burger_list:
            if burger.name == temp_list[i]:
                burger.meat = input("Enter new Burger meat (leave blank if no meat): ")
                burger.toppings = input("Enter new Burger toppings (separated by comma): ")
                burger.sauce = input("Enter new Burger sauce: ")
                if len(burger.meat) == 0:
                    burger.veggie = True
        print(f"\nBurger \"{temp_list[i]}\" has been changed.")
        save_data(burger_list)
    pause_app()


# Function to show all Burgers
def show_burgers(burger_list) -> None:
    if not burger_list:
        print("\nNo Burges found.")
        pause_app()
        return
    print("\nList of available Burgers: ")
    for burger in burger_list:
        print(f"\t{burger.name}:")
        if burger.veggie:
            print("\t(Veggie Burger)")
        print(f"\t\t{burger_stack[1]}: {burger.meat}")
        print(f"\t\t{burger_stack[3]}: {burger.toppings}")
        print(f"\t\t{burger_stack[4]}: {burger.sauce}")
    print("\n")
    pause_app()


# Function to search Burgers by name or ingredients
def search_burgers(burger_list) -> None:
    temp_dict = {}
    for burger in burger_list:
        temp_dict[burger.name] = (burger.meat + "," + ','.join(burger.toppings) + "," + burger.sauce).split(",")
    word_to_search = input("Type a string of characters to search: ")

    matches = [
        (burger_name, burger_pieces)
        for burger_name, burger_pieces in temp_dict.items()
        if word_to_search.lower() in burger_name.lower()
           or any(word_to_search.lower() in piece.lower() for piece in burger_pieces)
        # list comprehension and the any function
    ]
    if not matches:
        print(f"This string \"{word_to_search}\" not found.")
        return
    print(f"List of Burgers containing '{word_to_search}' in their name or ingredients:")
    for burger_name, burger_pieces in matches:
        for burger in burger_list:
            if burger.name == burger_name:
                print(f"\t{burger.name}:")
                if burger.veggie:
                    print("\t(Veggie Burger)")
                print(f"\t\t{burger_stack[1]}: {burger.meat}")
                print(f"\t\t{burger_stack[3]}: {burger.toppings}")
                print(f"\t\t{burger_stack[4]}: {burger.sauce}")
    print("\n")
    pause_app()


# Function to delete selected Burger
def delete_burger(burger_list) -> None:
    if not burger_list:
        print("\nNo Burges found.")
        pause_app()
        return
    print("\nList of Burgers: ")
    temp_list = []
    qty_of_burgers = 0
    for i, burger in enumerate(burger_list, start=1):
        temp_list.append(burger.name)
        print(f"\t{i}. {burger.name}")
        qty_of_burgers += 1

    chosen_burger = input(f"\nWhich Burger would you like to delete? Enter you choice (1-{qty_of_burgers}):")
    if not chosen_burger.isnumeric() or int(chosen_burger) > qty_of_burgers:
        print("Invalid choice!")
    else:
        i = int(chosen_burger)
        i -= 1
        for burger in burger_list:
            if burger.name == temp_list[i]:
                burger_list.pop(i)
        print(f"Burger \"{temp_list[i]}\" has been deleted.")
        save_data(burger_list)
    pause_app()


'''Main Function'''


def main():
    burgers = load_data_file(DATA_FILE)

    while valid_file:
        print("\t*****  Burger Manager *****")
        print("1. Add new Burger")
        print("2. Show Burgers")
        print("3. Search Burgers")
        print("4. Edit Burger")
        print("5. Delete Burger")
        print("Q. Exit")
        choice = input("Enter your choice (1-5) or Q to exit: ")
        if choice == "1":
            add_new_burger(burgers)
        elif choice == "2":
            show_burgers(burgers)
        elif choice == "3":
            search_burgers(burgers)
        elif choice == "4":
            edit_burger(burgers)
        elif choice == "5":
            delete_burger(burgers)
        elif choice.lower() == "q":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()