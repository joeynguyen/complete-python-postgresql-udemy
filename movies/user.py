class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {} movies: {}>".format(self.name, [movie for movie in self.movies])
