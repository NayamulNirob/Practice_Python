# This function takes any number of positional arguments and prints them in a formatted way.
# the function uses *args to accept a variable number of positional arguments, which are then iterated over using a for loop.
#the function *args accepts the values as tuple and prints each value on a new line. The function is then called with five arguments, which are printed in the order they were passed.
def practice (*args):
    for  value in args:
        print(value)
practice("John", 30, "New York", "Engineer", "Python Developer")
print("-------------args----------------")
practice("Jane", 28, "San Francisco", "Designer", "JavaScript Developer")
print("-------------args----------------")
practice("Mike", 35, "Chicago", "Manager", "Java Developer")
print("-------------args----------------")

#** This function takes any number of keyword arguments and prints them in a formatted way.
# the function uses **kwargs to accept a variable number of keyword arguments, which are then iterated over using a for loop.
#the function **kwargs accepts the values as a dictionary and prints each key-value pair in the format "key: value". The function is then called with six keyword arguments, which are printed in the order they were passed.
def practiceKwargs (**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

practiceKwargs(name="Alice",  age=25, city="Los Angeles", profession="Data Scientist", language="Python", framework="Django")
print("--------------kwargs---------------")
practiceKwargs(name="Bob",  age=32, city="Seattle", profession="Software Engineer", language="JavaScript", framework="React")
print("--------------kwargs---------------")
practiceKwargs(name="Charlie",  age=29, city="Austin", profession="Product Manager", language="Java", framework="Spring")