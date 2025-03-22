class Student:
    def __init__(self):
        self.height = 170
    height = 160
    def printer(self):
        print(self.height)
    def change_height(self, new_height):
        self.height = new_height
nick = Student()
nick.printer()
nick.change_height(174)
nick.printer()