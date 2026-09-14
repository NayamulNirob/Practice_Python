#Map&FilterFunction normally used in python to apply a function to all the items in an iterable (like a list) and return a new iterable with the results. The map() function takes two arguments: a function and an iterable. It applies the function to each item in the iterable and returns a new iterable with the results.
#The filter() function is used to filter items in an iterable based on a condition. It takes two arguments: a function and an iterable. It applies the function to each item in the iterable and returns a new iterable with only the items that satisfy the condition.
#In this example, we have a list of numbers and we want to square each number in

num=[1, 2, 3, 4, 5]
def square(x):
    return x * x
mapUse=list(map(square, num)) # The map() function applies the square function to each item in the num list and returns a new list with the squared values. The result is then converted to a list using the list() function and stored in the variable mapUse.
print("Map use with user define Function: ",mapUse)

squared_numbers = list(map(lambda x: x * x, num))
print("Map use with Lambda Function: ",squared_numbers)

print("-----------------Filter Function-------------------")
#In this example, we have a list of numbers and we want to filter out the even numbers from the list. We define a function is_even() that checks if a number is even.
def is_even(x):
    return x % 2 == 0
filterUse=list(filter(is_even, num)) # The filter() function applies the is_even function to each item in the num list and returns a new list with only the even numbers. The result is then converted to a list using the list() function and stored in the variable filterUse.
print("Filter use with user define Function: ",filterUse)
filterUseWithLambda=list(filter(lambda x: x % 2 == 0, num))
print("Filter use with Lambda Function: ",filterUseWithLambda)

print("-----------------List Comprehensions-------------------")
#List comprehensions are a concise way to create lists in Python. They allow you to generate a new list by applying an expression to each item in an existing iterable. The basic syntax of a list comprehension is as follows:
# [expression for item in iterable if condition]
squared_numbers_comprehension = [x * x for x in num]
print("List comprehension for squaring numbers: ", squared_numbers_comprehension)

even_numbers_comprehension = [x for x in num if x % 2 == 0]
print("List comprehension for even numbers: ", even_numbers_comprehension)