class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    def __len__(self):
        return self.duration   
movie = Movie("Interstellar", 169)

print(len(movie))
print(movie.__len__())