class Movie:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def __repr__(self):
        return '<Movie name="{}" genre="{}">'.format(self.name, self.genre)
