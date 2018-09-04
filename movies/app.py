from movie import Movie
from user import User

username = 'Joe'
user = User(username)
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
print('user json', user.json())
user.save_to_json()
json_data = User.read_from_json(username + '.json')
print('json_data', json_data)

print("")
print("Saving to file...")
user.save_to_file()

print("")
print("Reading from file...")
my_user = User.read_user_data_from_file(username + '.csv')
print('my_user', my_user.name)
print('my_user movies', my_user.movies)
print('my_user watched movies', my_user.get_watched_movies())
