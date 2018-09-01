from movie import Movie
from user import User

my_movie = Movie('The Matrix', 'Sci-Fi')

user = User('Joe')
user.movies.append(my_movie)
print(user)
