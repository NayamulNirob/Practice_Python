import math

#Triangle calculation
#formula: Area = 1/2 * base * height

base=float(input("Enter the base of the triangle: "))
height=float(input("Enter the height of the triangle: "))
area=0.5*base*height
print(f"The area of the triangle is: {area}")


#Rectangle calculation
#formula: Area = length * width

length = float(input("Enter the length of the triangle: "))
width = float(input("Enter the width of the triangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")


#Trapezoid calculation
#formula: Area = 1/2 * (base1 + base2) * height

base1 = float(input("Enter the first base of the trapezoid: "))
base2 = float(input("Enter the second base of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
area = 0.5 * (base1 + base2) * height
print(f"The area of the trapezoid is: {area}")


#Elipse calculation
#formula: Area = π * a * b
#formula: Area = 3.14159 * a * b

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
area=math.pi*a*b
print(f"The area of the ellipse is: {area}")


#Square calculation
#formula: Area = side * side

side = float(input("Enter the side of the square: "))
area = side * side
print(f"The area of the square is: {area}")

#Perallogram calculation
#formula: Area = base * height
base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))
area = base * height
print(f"The area of the parallelogram is: {area}")

#Circle calculation
#formula: Area = π * r^2
#formula: Area = 3.14159 * r^2
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle is: {area}")

#Sector calculation
#formula: Area = 1/2 * π * r^2
#formula: Area = 1/2 * 3.14159 * r^2
theta = float(input("Enter the angle in degrees: "))
radius = float(input("Enter the radius of the sector: "))
area = 0.5 * math.pi * radius ** 2
print(f"The area of the sector is: {area}")