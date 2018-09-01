class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def get_watched_movies(self):
        watched_movies = list(filter(lambda x: x.watched, self.movies))

        return watched_movies
