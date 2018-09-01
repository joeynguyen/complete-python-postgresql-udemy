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
