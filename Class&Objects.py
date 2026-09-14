import logging
logging.basicConfig(level=logging.DEBUG)


class Student:
        name=""
        age=0

rohim=Student()
rohim.name="Rohim"
rohim.age=25
print(f"Name: {rohim.name}, Age: {rohim.age}")

karim=Student()
karim.name="Karim"
karim.age=20
print(f"Name: {karim.name}, Age: {karim.age}")


class Teacher:
    def __init__(self,name,age,subject):
        self.name=name
        self.age=age
        self.subject=subject

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}")

abdul=Teacher("Abdul",21,"C")
abdul.display()

jobbar=Teacher("Jobbar",22,"C++")
jobbar.display()


class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def calculate_area(self):
        return  0.5 * self.base * self.height


areaCalculator1=Triangle(10,20)
logging.info(areaCalculator1.calculate_area())

areaCalculator2=Triangle(20,30)
logging.info(areaCalculator2.calculate_area())