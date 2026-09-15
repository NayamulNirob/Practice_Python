a= 20
b=10
# temp=0
# temp=a # temp =20
# a=b # a =10
# b=temp # b =20
# print("The value of a after swapping: ",a)
# print("The value of b after swapping: ",b)

#Easy way to swap two numbers in python
a,b=b,a
print("The value of a after swapping: ",a)
print("The value of b after swapping: ",b)


#Example of Global variable and how to reassign the value.
x=50
def fun1():
  global x
  x=20
  return x

fun1()
print(x)


