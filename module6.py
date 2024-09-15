# movie preferences
comedy = input("Do you like watching comedy movies? (yes / no): ").lower() == "yes"
horror = input("Do you like watching horror movies? (yes / no): ").lower() == "yes"
drama = input("Do you like watching drama movies? (yes / no): ").lower() == "yes"
thriller = input("Do you like watching thiller movies? (yes / no): ").lower() == "yes"

#Combine the booleans using logical operators to determine the movie genre.
if comedy and horror and not drama:
    genre = "Horror-Comedy"
elif comedy and drama and not horror:
    genre = "Comedy-Drama"
elif horror and drama and not comedy:
    genre = "Horror- drama"
elif comedy:
    genre = "Comedy"
elif horror:
    genre = "Horror"
elif drama:
    genre = "Drama"
elif thriller:
    genre = "Thriller"



# Recommend movies based on the genre using conditional statements
if genre == "Horror-Comedy":
    print("Recommended movies: 'Scary Movie, Lisa Frankenstein, The dead do not die'")
elif genre == "Comedy-Drama":
    print("Recommended movies: 'Fly Me to the Moon, Another Round, The Fail Guy'")
elif genre == "Horror - Drama":
    print("Recommended movies: 'Take Shelter, The Platform,  High Life'")
elif genre == "Comedy":
    print("Recommended movies: 'Hangover, Dumb and Dumber, Wedding Crashers'")
elif genre == "Horror":
    print("Recommended movies: 'The Exorcist, X, IT'")
elif genre == "Drama":
    print("Recommended movies: 'Pieces of Woman, Leave no Trace, Shame '")
elif genre == "Thriller":
    print("Recomended movies: Union, Gone Girl, Seven")
else:
    print("Sorry, we couldn't determine your movie preferences.")

