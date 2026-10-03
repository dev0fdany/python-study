class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return "Student({}, {})".format(self.name, self.grade)
    def __str__(self):
        return "{} - {}".format(self.name, self.grade)

s = Student("Ali", "A")

print(repr(s))
print(s)