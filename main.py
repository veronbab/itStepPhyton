class Student:
    amount_of_students = 0
    def __init__(self, height=160):
        self.height = height
        Student.amount_of_students += 1

print(Student.amount_of_students)
nick = Student()
kate = Student(height=165)
print(nick.amount_of_students)
print(Student.amount_of_students)

