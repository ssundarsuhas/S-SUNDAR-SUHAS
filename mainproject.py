# MOVIE RECOMMENDATION SYSTEM
# Python Essentials Project
import random 

action_movies = [
    ["The Dark Knight", 9.0, 2008, "English"],
    ["The Lord of the Rings Trilogy", 9.0, 2001, "English"],
    ["The Good, the Bad and the Ugly", 8.8, 1966, "Italian"],
    ["Terminator 2: Judgment Day", 8.6, 1991, "English"],
    ["Saving Private Ryan", 8.6, 1998, "English"],
    ["Django Unchained", 8.5, 2012, "English"],
    ["Inglourious Basterds", 8.4, 2009, "English"],
    ["Avengers: Endgame (MCU)", 8.4, 2019, "English"],
    ["Heat", 8.3, 1995, "English"],
    ["Top Gun: Maverick", 8.2, 2022, "English"],
    ["KGF: Chapter 1", 8.2, 2018, "Kannada"],
    ["Mad Max: Fury Road", 8.1, 2015, "English"],
    ["Ford v Ferrari", 8.1, 2019, "English"],
    ["The Terminator", 8.0, 1984, "English"],
    ["Baahubali: The Beginning", 8.0, 2015, "Telugu"],
    ["Harry Potter Series", 7.9, 2001, "English"],
    ["RRR", 7.8, 2022, "Telugu"],
    ["F1", 7.7, 2025, "English"],
    ["Spider-Man (Sam Raimi)", 7.4, 2002, "English"],
    ["John Wick", 7.4, 2014, "English"],
    ["DCEU (Man of Steel)", 7.1, 2013, "English"],
    ["The Amazing Spider-Man", 6.9, 2012, "English"]
]

sci_fi_movies = [
    ["Inception", 8.8, 2010, "English"],
    ["Interstellar", 8.7, 2014, "English"],
    ["The Matrix", 8.7, 1999, "English"],
    ["Back to the Future", 8.5, 1985, "English"],
    ["Alien", 8.5, 1979, "English"],
    ["Dune Series", 8.5, 2021, "English"],
    ["Aliens", 8.4, 1986, "English"],
    ["A Clockwork Orange", 8.3, 1971, "English"],
    ["2001: A Space Odyssey", 8.3, 1968, "English"],
    ["Project Hail Mary", 8.3, 2026, "English"],
    ["Avatar Series", 7.9, 2009, "English"]
]

drama_movies = [
    ["The Shawshank Redemption", 9.3, 1994, "English"],
    ["The Godfather", 9.2, 1972, "English"],
    ["12 Angry Men", 9.0, 1957, "English"],
    ["Schindler's List", 9.0, 1993, "English"],
    ["Forrest Gump", 8.8, 1994, "English"],
    ["12th Fail", 8.8, 2023, "Hindi"],
    ["Goodfellas", 8.7, 1990, "English"],
    ["One Flew Over the Cuckoo's Nest", 8.7, 1975, "English"],
    ["The Green Mile", 8.6, 1999, "English"],
    ["It's a Wonderful Life", 8.6, 1946, "English"],
    ["Life Is Beautiful", 8.6, 1997, "Italian"],
    ["Parasite", 8.5, 2019, "Korean"],
    ["Cinema Paradiso", 8.5, 1988, "Italian"],
    ["Whiplash", 8.5, 2014, "English"],
    ["The Lives of Others", 8.4, 2006, "German"],
    ["Capernaum", 8.4, 2018, "Arabic"],
    ["Oppenheimer", 8.3, 2023, "English"],
    ["Scarface", 8.3, 1983, "English"],
    ["Dangal", 8.3, 2016, "Hindi"],
    ["Good Will Hunting", 8.3, 1997, "English"],
    ["Once Upon a Time in America", 8.3, 1984, "English"],
    ["Requiem for a Dream", 8.3, 2000, "English"],
    ["Incendies", 8.3, 2010, "French"],
    ["The Wolf of Wall Street", 8.2, 2013, "English"],
    ["Green Book", 8.2, 2018, "English"],
    ["Dead Poets Society", 8.1, 1989, "English"],
    ["Raging Bull", 8.1, 1980, "English"],
    ["Into the Wild", 8.1, 2007, "English"],
    ["Stand by Me", 8.1, 1986, "English"],
    ["Catch Me If You Can", 8.1, 2002, "English"],
    ["Trainspotting", 8.1, 1996, "English"],
    ["The Perks of Being a Wallflower", 7.9, 2012, "English"],
    ["The Social Network", 7.8, 2010, "English"]
]

thriller_movies = [
    ["Fight Club", 8.8, 1999, "English"],
    ["Se7en", 8.6, 1995, "English"],
    ["The Silence of the Lambs", 8.6, 1991, "English"],
    ["Leon: The Professional", 8.5, 1994, "English"],
    ["The Usual Suspects", 8.5, 1995, "English"],
    ["The Prestige", 8.5, 2006, "English"],
    ["The Departed", 8.5, 2006, "English"],
    ["Rear Window", 8.5, 1954, "English"],
    ["Oldboy", 8.4, 2003, "Korean"],
    ["The Shining", 8.4, 1980, "English"],
    ["Memento", 8.4, 2000, "English"],
    ["Maharaja", 8.4, 2024, "Tamil"],
    ["Andhadhun", 8.2, 2018, "Hindi"],
    ["Shutter Island", 8.2, 2010, "English"],
    ["L.A. Confidential", 8.2, 1997, "English"],
    ["No Country for Old Men", 8.2, 2007, "English"],
    ["Memories of Murder", 8.1, 2003, "Korean"],
    ["Gone Girl", 8.1, 2014, "English"],
    ["The Exorcist", 8.1, 1973, "English"]
]

comedy_movies = [
    ["The Intouchables", 8.5, 2011, "French"],
    ["3 Idiots", 8.4, 2009, "Hindi"],
    ["The Truman Show", 8.2, 1998, "English"],
    ["The Grand Budapest Hotel", 8.1, 2014, "English"],
    ["The Hangover", 7.7, 2009, "English"],
    ["Premalu", 7.6, 2024, "Malayalam"],
    ["Superbad", 7.6, 2007, "English"],
    ["The Secret Life of Walter Mitty", 7.3, 2013, "English"]
]

romance_movies = [
    ["Casablanca", 8.5, 1942, "English"],
    ["Amelie", 8.3, 2001, "French"],
    ["Eternal Sunshine of the Spotless Mind", 8.3, 2004, "English"],
    ["Before Sunrise Series", 8.1, 1995, "English"],
    ["Hridayam", 8.1, 2022, "Malayalam"],
    ["Charlie", 8.0, 2015, "Malayalam"],
    ["Titanic", 7.9, 1997, "English"],
    ["About Time", 7.8, 2013, "English"],
    ["The Lunchbox", 7.8, 2013, "Hindi"],
    ["500 Days of Summer", 7.7, 2009, "English"]
]

animation_movies = [
    ["Grave of the Fireflies", 8.5, 1988, "Japanese"],
    ["Spider-Man: Into the Spider-Verse", 8.4, 2018, "English"],
    ["Your Name", 8.4, 2016, "Japanese"],
    ["Coco", 8.4, 2017, "English"],
    ["WALL-E", 8.4, 2008, "English"],
    ["Toy Story Series", 8.3, 1995, "English"],
    ["Up", 8.3, 2009, "English"],
    ["Princess Mononoke", 8.3, 1997, "Japanese"],
    ["Klaus", 8.2, 2019, "English"],
    ["Finding Nemo", 8.2, 2003, "English"],
    ["A Silent Voice", 8.1, 2016, "Japanese"],
    ["Inside Out", 8.1, 2015, "English"],
    ["Ratatouille", 8.1, 2007, "English"],
    ["How to Train Your Dragon Series", 8.1, 2010, "English"],
    ["Zootopia", 8.0, 2016, "English"],
    ["Chainsaw Man: Reze Arc", 8.0, 2025, "Japanese"],
    ["I Want to Eat Your Pancreas", 7.6, 2018, "Japanese"],
    ["Kung Fu Panda Series", 7.5, 2008, "English"],
    ["Cars Series", 7.1, 2006, "English"]
]

watchlist = []

def welcome_screen():
    print("      MOVIE RECOMMENDATION SYSTEM")
    print("Confused about what you're gonna watch?")
    print()
    while True:
        answer = input("Do you want a movie recommendation? (yes/no): ")
        answer = answer.strip().lower()

        if answer == "yes":
            print()
            print("Then you are at the right place!")
            break
        elif answer == "no":
            print()
            print("Why are you even here?")
            print("Go watch those brainrot reels!!")
            input("Press Enter to try again...")
            print()
        else:
            print("Please enter yes or no only.")
            print()


def show_movies(movie_list, genre_name):
    print()
    print("---------- " + genre_name + " Movies ----------")

    number = 1
    for movie in movie_list:
        print(str(number) + ". " + movie[0])
        print("   Rating:", movie[1], "| Year:", movie[2], "| Language:", movie[3])
        number = number + 1


def genre_menu():
    print()
    print("---------- GENRES ----------")
    print("1. Action")
    print("2. Sci-Fi")
    print("3. Drama")
    print("4. Thriller")
    print("5. Comedy")
    print("6. Romance")
    print("7. Animation")

    choice = input("Choose a genre (1-7): ")

    if choice == "1":
        show_movies(action_movies, "Action")
    elif choice == "2":
        show_movies(sci_fi_movies, "Sci-Fi")
    elif choice == "3":
        show_movies(drama_movies, "Drama")
    elif choice == "4":
        show_movies(thriller_movies, "Thriller")
    elif choice == "5":
        show_movies(comedy_movies, "Comedy")
    elif choice == "6":
        show_movies(romance_movies, "Romance")
    elif choice == "7":
        show_movies(animation_movies, "Animation")
    else:
        print("Invalid choice! Please enter a number from 1 to 7.")


def get_all_movies():
    
    all_movies = (action_movies + sci_fi_movies + drama_movies + thriller_movies
                  + comedy_movies + romance_movies + animation_movies)
    return all_movies


def show_top_rated():
    all_movies = get_all_movies()

    print()
    print("---------- TOP 10 RATED MOVIES ----------")

    for rank in range(1, 11):
        best_index = 0
        for i in range(len(all_movies)):
            if all_movies[i][1] > all_movies[best_index][1]:
                best_index = i

        best_movie = all_movies[best_index]
        print(str(rank) + ". " + best_movie[0])
        print("   Rating:", best_movie[1], "| Year:", best_movie[2], "| Language:", best_movie[3])
        all_movies.remove(best_movie)


def random_movie():
    all_movies = get_all_movies()
    movie = random.choice(all_movies)

    print()
    print("---------- RANDOM MOVIE ----------")
    print("How about watching this one?")
    print(movie[0])
    print("Rating:", movie[1], "| Year:", movie[2], "| Language:", movie[3])


def filter_by_language():
    print()
    print("Languages: English, Hindi, Malayalam, Tamil, Telugu, Kannada,")
    print("Korean, Japanese, French, Italian, German, Arabic")
    language = input("Enter a language: ")
    language = language.strip().lower()

    all_movies = get_all_movies()
    count = 0

    print()
    print("---------- " + language.capitalize() + " Movies ----------")

    for movie in all_movies:
        if movie[3].lower() == language:
            count = count + 1
            print(str(count) + ". " + movie[0])
            print("   Rating:", movie[1], "| Year:", movie[2], "| Language:", movie[3])
    if count == 0:
        print("No movies found in this language.")


def watchlist_menu():
    while True:
        print()
        print("---------- MY WATCHLIST ----------")
        print("1. Add a movie to my watchlist")
        print("2. View my watchlist")
        print("3. Back to main menu")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            name = input("Enter the movie name: ")
            name = name.strip()
            if name == "":
                print("You did not type anything!")
            elif name in watchlist:
                print("This movie is already in your watchlist.")
            else:
                watchlist.append(name)
                print(name + " added to your watchlist!")
        elif choice == "2":
            if len(watchlist) == 0:
                print("Your watchlist is empty.")
            else:
                print()
                print("Your watchlist:")
                number = 1
                for name in watchlist:
                    print(str(number) + ". " + name)
                    number = number + 1
        elif choice == "3":
            break
        else:
            print("Invalid choice! Please enter 1, 2 or 3.")


def main_menu():
    while True:
        print()
        print("---------- MAIN MENU ----------")
        print("1. Browse movies by genre")
        print("2. Show top rated movies")
        print("3. Get a random movie")
        print("4. Filter movies by language")
        print("5. My watchlist")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            genre_menu()
        elif choice == "2":
            show_top_rated()
        elif choice == "3":
            random_movie()
        elif choice == "4":
            filter_by_language()
        elif choice == "5":
            watchlist_menu()
        elif choice == "6":
            print()
            print("Thank you for using the Movie Recommendation System!")
            print("Enjoy your movie. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 6.")

welcome_screen()
main_menu()