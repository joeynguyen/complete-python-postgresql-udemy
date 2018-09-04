import json
from movie import Movie
class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre):
        self.movies.append(Movie(name, genre, False))

    def delete_movie(self, movie_name):
        movies_to_not_delete = list(filter(lambda x: x.name != movie_name, self.movies))
        self.movies = movies_to_not_delete

    def watch_movie(self, movie_name):
        movie = list(filter(lambda x: x.name == movie_name, self.movies))
        if len(movie) == 1:
            movie[0].mark_movie_watched(True)

    def get_watched_movies(self):
        watched_movies = list(filter(lambda x: x.watched, self.movies))
        return watched_movies

    def save_to_file(self):
        file_name = self.name + '.csv'
        with open(file_name, 'w') as f:
            f.write(self.name + '\n')
            for movie in self.movies:
                movie_details = [movie.name, movie.genre, str(movie.watched)]
                f.write(','.join(movie_details) + '\n')

    @classmethod
    def read_user_data_from_file(cls, file_name):
        with open(file_name, 'r') as f:
            content = f.readlines()
            # content[0] is first line of file
            username = content[0]
            user_movies = []
            # start loop from second line until end of file
            for line in content[1:]:
                line = line.strip() # remove whitespace (new line code '\n')
                movie_data = line.split(',')
                # last argument is converted string to boolean
                movie = Movie(movie_data[0], movie_data[1], movie_data[2] == 'True')
                user_movies.append(movie)

            user = cls(username)
            user.movies = user_movies
            return user

    def json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    def save_to_json(self):
        with open ('my_file.json', 'w') as f:
            json.dump(self.json(), f)
