class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return '<Movie name="{}" genre="{}" watched="{}">'.format(self.name, self.genre, self.watched)
