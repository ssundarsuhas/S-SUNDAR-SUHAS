# Movie Recommendation System

This is my Python Essentials project. It is a simple movie recommendation program that runs in the terminal. It helps you decide what to watch.

## What it can do

- Browse movies by genre (Action, Sci-Fi, Drama, Thriller, Comedy, Romance, Animation)
- Show the top 10 rated movies
- Give a random movie
- Show movies of a language you type (like Hindi or Japanese)
- Keep a watchlist where you can add and view movies
- Exit

There are 122 movies in the program. For each movie it shows the name, rating, year and language.

## How to run

You need Python 3 installed. Then open a terminal in the folder where main.py is and type:

```
python main.py
```

If that doesn't work, try `python3 main.py`. I didn't use any extra libraries, only the built-in `random` module.

## How the program works

When the program starts it asks "Do you want a movie recommendation? (yes/no)". If you type yes it goes to the main menu. If you type no it shows a funny message and asks again. If you type anything else it asks you to enter yes or no.

The main menu looks like this:

```
1. Browse movies by genre
2. Show top rated movies
3. Get a random movie
4. Filter movies by language
5. My watchlist
6. Exit
```

The menu keeps coming back after every option until you choose 6.

## How the movies are stored

Every movie is a list with 4 things:

```
["The Dark Knight", 9.0, 2008, "English"]
```

- movie[0] = name
- movie[1] = rating
- movie[2] = year
- movie[3] = language

All the movies of one genre are kept in one big list (like action_movies, drama_movies etc). The ratings are approximate IMDb ratings. For series like Harry Potter I used one entry with the rating and year of the main or first movie.

## How the top 10 works

I didn't use sort. Instead I used a loop:

1. Join all the genre lists into one list
2. Assume the first movie is the best
3. Go through all the movies and if any has a higher rating, remember it
4. Print that movie and remove it from the list
5. Do this 10 times

## Things I used

- lists
- for loops and while loops
- if / elif / else
- functions
- input() and print()
- strip(), lower(), capitalize()
- append() and remove()
- the random module

## Limitations

- The watchlist is not saved. When you close the program it becomes empty again.
- The movies are fixed. To add a new movie you have to add a line in main.py, like this:

```
["Movie Name", 8.0, 2020, "English"],
```

## Made by

Name: S SUNDAR SUHAS
B.Tech CSE CORE, First Year
Registration No. : 26BCE11114
Subject: Python Essentials
