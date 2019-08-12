import os
import json
from user import User


def menu():
    name = input('Enter your name: ')
    filename = '{}.txt'.format(name)
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.read_from_json(json_data)
    else:
        user = User(name)

    selection = input(selection_text)

    while selection != 'q':
        if selection == 'a':
            movie_name = input("Enter the movie name: ")
            movie_genre = input("Enter the movie genre: ")
            user.add_movie(movie_name, movie_genre)
        elif selection == 's':
            for movie in user.movies:
                print("Name: {} Genre: {} Watched: {}.".format(movie.name, movie.genre, movie.watched))
        elif selection == 'w':
            movie_name = input("Enter the movie name to be set as watched ")
            user.watch_movie(movie_name)
        elif selection == 'd':
            movie_name = input("Enter the movie name to delete ")
            user.delete_movie(movie_name)
        elif selection == 'l':
            for movie in user.get_watched_movies():
                print("Name: {} Genre: {} Watched: {}.".format(movie.name, movie.genre, movie.watched))

        selection = input(selection_text)

    with open(filename, 'w') as f:
        json.dump(user.json(), f)

selection_text = """
    Enter 'a' to add a movie,
    's' to see the list of movies,
    'w' to set a movie as watched,
    'd' to delete a movie,
    'l' to see the list of movies watched,
    or 'q' to save and quit.
    Enter your selection: """

def file_exists(filename):
    return os.path.isfile(filename)

menu()

# import json
# from movie import Movie
# from user import User

# username = 'Joe'
# user = User(username)
# user.add_movie('The Matrix', 'Sci-Fi')
# user.add_movie('Spirited Away', 'Fantasy')
# user.add_movie('Zoolander', 'Comedy')

# user.watch_movie('Spirited Away')

# print(user)
# print("Movies collection: ", user.movies)
# print("Watched movies: ", user.get_watched_movies())

# print("")
# print("Deleted 'The Matrix'")
# user.delete_movie('The Matrix')
# print(user)
# print("Movies collection: ", user.movies)
# print("Watched movies: ", user.get_watched_movies())
# print('user json', user.json())
# user.save_to_json()
# with open(username + '.json', 'r') as f:
#     json_data = json.load(f)
#     user = User.read_from_json(json_data)
#     print('json_data', user.json())


# print("")
# print("Saving to file...")
# user.save_to_file()

# print("")
# print("Reading from file...")
# my_user = User.read_user_data_from_file(username + '.csv')
# print('my_user', my_user.name)
# print('my_user movies', my_user.movies)
# print('my_user watched movies', my_user.get_watched_movies())
