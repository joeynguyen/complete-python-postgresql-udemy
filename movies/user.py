class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {} movies: {}>".format(self.name, [movie for movie in self.movies])

    def get_watched_movies(self):
        watched_movies = []
        for movie in self.movies:
            if movie.watched == True:
                watched_movies.append(movie)

        return watched_movies
