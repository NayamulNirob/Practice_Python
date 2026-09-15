class Shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @staticmethod
    def area():
        print("This a demo")


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