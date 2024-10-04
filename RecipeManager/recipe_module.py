class Burger:
    def __init__(self, name):
        self.name = name
        self.toppings = None
        self.meat = ""
        self.sauce = ""
        self.veggie = False
    
    def __str__(self) -> str:
        return self.name
        
    def show_burger(self):
        print(self.name)
    
    def add_topping(self, toppings):
        self.toppings.append(toppings)