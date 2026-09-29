# Movie Recommendation System

## 1. Problem Statement

Choosing a movie to watch can be difficult when there are many movies available across different genres and languages. Users may spend a lot of time deciding what to watch.

The Movie Recommendation System is a simple Python-based command-line application that helps users discover movies through different options such as genre browsing, top-rated movies, random movie selection, language filtering, and a personal watchlist.

## 2. Scope of the Project

The project is limited to a terminal-based movie recommendation and browsing system developed using Python.

The system includes:
- Movies organized into seven genres: Action, Sci-Fi, Drama, Thriller, Comedy, Romance, and Animation.
- Movie information including name, rating, release year, and language.
- Top 10 rated movie selection.
- Random movie selection.
- Filtering movies by language.
- An in-memory watchlist for adding and viewing movie names.
- Menu-based interaction and basic input validation.

The current system does not use a database, machine learning, external APIs, or permanent watchlist storage.

## 3. Target Users

The system is intended for:
- Students learning Python programming.
- Users who want a simple way to browse and discover movies.
- Movie viewers who want suggestions based on genre, rating, language, or random selection.
- Beginners who prefer a simple command-line application instead of a complex graphical interface.

## 4. High-Level Features

### 1. Browse Movies by Genre
Users can select from seven genres and view the movies available in that genre along with their ratings, release years, and languages.

### 2. Show Top Rated Movies
The system finds and displays the top 10 highest-rated movies from the complete movie collection.

### 3. Get a Random Movie
The system randomly selects one movie from the complete movie collection using Python's `random` module.

### 4. Filter Movies by Language
Users can enter a language and view movies available in that language.

### 5. My Watchlist
Users can add movie names to a temporary watchlist and view the movies they have added during the current program session.

### 6. Interactive Menu
The system provides a main menu and separate menus for genres and the watchlist, with messages for invalid choices.
