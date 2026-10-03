class Student:
    passing_mark = 40
    num_of_students = 0
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        Student.num_of_students +=1

    @classmethod
    def change_passing_mark(cls, n):
        cls.passing_mark = n
        print("Passing Mark: {}".format(cls.passing_mark))

    @staticmethod
    def grade(mark):
        if mark > 90:
            print("A")
        elif mark > 80:
            print("B")
        elif mark > 70:
            print("C")
        else:
            print("D")

    def description(self):
        return"{} has {} marks.".format(self.name, self.mark)

s1 = Student("Ali", 82)
s2 = Student("James", 73)

print(Student.passing_mark)
Student.change_passing_mark(35)

print(s1.description())
Student.grade(80)
print(s2.description())
print(Student.num_of_students)

