class Human:
    name = "john"
    age = 0
    def speak(self):
        print(f"My name is {self.name} and my age is {self.age}")


class Student:
    grade = 2
    def speak(self):
        print(f"My name is {self.name} and my age is {self.age}. I study in grade {self.grade}")



def Main():
    me = Human()
    me.name = "Geetesh"
    me.age = 19
    print(me.name,me.age)
    me.speak()


    gudiya = Student()
    gudiya.name = "Gudiya"
    gudiya.age = 18
    gudiya.grade = 12

    gudiya.speak()

if __name__ == "__main__":
    Main()
