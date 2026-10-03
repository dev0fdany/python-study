class Book:
    def __init__(self,title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return "{} book by {}, and has {} pages".format(self.title,self.author,self.pages)

book1 = Book("Atomic Habits","James Clear", 320)
book2 = Book("The Metamorphosis", "Franz Kafka", 77)
book3 = Book("No Longer Human","Dazai Osamu", 82)

print(book1.description())
print(book2.description())
print(book3.description())
