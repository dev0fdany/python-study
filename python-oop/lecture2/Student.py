class Student:
    num_of_students = 0
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.num_of_students +=1

    def description(self):
        return"{} is in grade {}".format(self.name, self.grade)

s1 = Student("Ali", 8)
s2 = Student("James", 12)

print(s1.description())
print(s2.description())
print(Student.num_of_students)