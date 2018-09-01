from movie import Movie
from user import User

my_movie = Movie('The Matrix', 'Sci-Fi', True)

user = User('Joe')
user.movies.append(my_movie)
print(user)
print("Watched movies: ", user.get_watched_movies())
