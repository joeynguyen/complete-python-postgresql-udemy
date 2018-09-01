from movie import Movie
from user import User

user = User('Joe')
user.add_movie('The Matrix', 'Sci-Fi')
user.add_movie('Spirited Away', 'Fantasy')
user.add_movie('Zoolander', 'Comedy')

user.watch_movie('Spirited Away')


print(user)
print("Movies collection: ", user.movies)
print("Watched movies: ", user.get_watched_movies())

print("")
print("Deleted 'The Matrix'")
user.delete_movie('The Matrix')
print(user)
print("Movies collection: ", user.movies)
print("Watched movies: ", user.get_watched_movies())
