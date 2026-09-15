# ** HIERARCHICAL Inheritance= Parent class can be inherited by multiple child classes  like this class.
# ** Multilevel Inheritance= Like A,B,C classes. B class inherit A class and C class inherit B class.
# ** Multiple Inheritance = A,B,C,D classes. A <-B, A <-C and D inherit B,C is called multiple Inheritance.

from abc import ABC,abstractmethod
# Abstract class is not allowed to create any object
# If any class inherit abstract class then that class must be the abstract method.

class Shape(ABC): #Example of abstract class
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self): # example of abstract method
        pass




class Triangle(Shape):
    def area(self):
        result= 0.5*self.dim1*self.dim2
        return print(f"The area of Triangle :{result}")


class Rectangle(Shape):
    def area(self):
        result= self.dim2*self.dim1
        return print(f"The area of Rectangle :{result}")

t1= Triangle(20,30)
t1.area()


r1 = Rectangle(10,20)
r1.area()