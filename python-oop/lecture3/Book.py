class Book:
    def __init__(self,title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price

    def description(self):
        return "{} book by {}, and is {}$".format(self.title,self.author,self.price)
    
    @classmethod
    def from_string(cls, book_str):
        title, author, price = book_str.split("-")
        return cls(title, author, price)

book1 = Book("Atomic Habits","James Clear", 16)
book2 = Book("The Metamorphosis", "Franz Kafka", 16)
book3 = Book("No Longer Human","Dazai Osamu", 15.65)

book_str = "Dune-Frank Herbert-12.50"
book4 = Book.from_string(book_str)

print(book1.description())
print(book2.description())
print(book3.description())
print(book4.description())
