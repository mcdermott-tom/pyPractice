class Student:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    def namePrint(self):
        print("Hey I'm "+self.name)

s = Student("Tom", 12)

s.namePrint()
s.name = "Tyler"
s.namePrint()