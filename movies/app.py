from movie import Movie
from user import User

the_matrix = Movie('The Matrix', 'Sci-Fi', True)
spirited_away = Movie('Spirited Away', 'Fantasy', False)
zoolander = Movie('Zoolander', 'Comedy', True)

user = User('Joe')
user.movies.extend([the_matrix, spirited_away, zoolander])
print(user)
print("Movies collection: ", user.movies)
print("Watched movies: ", user.get_watched_movies())
