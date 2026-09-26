"""
Midterm Practical Exam — Movie Collection Manager
Student: Cruz, Jan Andrei O.
"""

movies = []
director = []
status = []


def display_menu(movie_list):
    print("=== Movie Collection Manager ===")
    num1 = input(" 1. Add a movie ")
    num2 = input(" 2. View all movies ")
    num3 = input(" 3. Count Watched vs Unwatched ")
    num4 = input(" 4. Find a Movie ")
    num5 = input(" 5. Exit ")
    result = num1, num2, num3, num4, num5
    print(f"{result} Choose an option")
    pass

def add_movie(movie_list):
    # ask for title, director, and status
    title = input(" Enter the Movie Title: ")
    director = input(" Enter the Director of the Movie: ")
    status = input(" Enter if the Movie is Watched or ")

    # build the movie dictionary
    # add it to the list
    movie_list.append({
        'title': title,
        'director': director,
        'status': status
    })
    print("Movie added successfully.")


def view_movies(movie_list):
    print(" === All Movies === ")
    movietitle = [movies]
    directors = [director]
    moviestatus = [status]
    
    # loop through and print every movie
    for index, movies in enumerate(movietitle):
        print(f"Index {index}: {movietitle}")
    for index, director in enumerate(directors):
        print(f"Index {index}: {directors}")
    for index, status in enumerate(moviestatus):
        print(f"Index {index}: {moviestatus}")
    # handle empty list
    else: 
        print("No movies in the collection.")
    pass


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


def main():
    # create the main menu loop
    # call the appropriate function based on the user's choice
    pass


main()
