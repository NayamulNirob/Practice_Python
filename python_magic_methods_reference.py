"""
Python Magic (Dunder) Methods Reference
========================================

Magic methods are special methods whose names start and end with __.
They allow custom classes to work naturally with Python syntax and
built-in functions.

This file contains common magic methods with short examples.
"""


# ============================================================
# 1. OBJECT CREATION AND INITIALIZATION
# ============================================================

class Person:
    def __new__(cls, name):
        print("__new__(): Creating the object")
        return super().__new__(cls)

    def __init__(self, name):
        print("__init__(): Initializing the object")
        self.name = name

    def __del__(self):
        print("__del__(): Object is being destroyed")


# Example:
# person = Person("Nayamul")


# ============================================================
# 2. STRING REPRESENTATION
# ============================================================

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        """User-friendly representation: called by print()."""
        return f"Student(name={self.name}, marks={self.marks})"

    def __repr__(self):
        """Developer-friendly representation: useful for debugging."""
        return f"Student({self.name!r}, {self.marks!r})"


# Example:
# student = Student("Nayamul", 85)
# print(student)          # __str__()
# print(repr(student))    # __repr__()


# ============================================================
# 3. COMPARISON METHODS
# ============================================================

class Number:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """=="""
        return self.value == other.value

    def __ne__(self, other):
        """!="""
        return self.value != other.value

    def __lt__(self, other):
        """<"""
        return self.value < other.value

    def __le__(self, other):
        """<="""
        return self.value <= other.value

    def __gt__(self, other):
        """>"""
        return self.value > other.value

    def __ge__(self, other):
        """>="""
        return self.value >= other.value


# Example:
# a = Number(10)
# b = Number(20)
# print(a == b)
# print(a < b)
# print(a > b)


# ============================================================
# 4. ARITHMETIC OPERATOR METHODS
# ============================================================

class CalculatorNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        """+"""
        return CalculatorNumber(self.value + other.value)

    def __sub__(self, other):
        """-"""
        return CalculatorNumber(self.value - other.value)

    def __mul__(self, other):
        """*"""
        return CalculatorNumber(self.value * other.value)

    def __truediv__(self, other):
        """/"""
        return CalculatorNumber(self.value / other.value)

    def __floordiv__(self, other):
        """//"""
        return CalculatorNumber(self.value // other.value)

    def __mod__(self, other):
        """%"""
        return CalculatorNumber(self.value % other.value)

    def __pow__(self, other):
        """**"""
        return CalculatorNumber(self.value ** other.value)

    def __str__(self):
        return str(self.value)


# Example:
# a = CalculatorNumber(10)
# b = CalculatorNumber(3)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)


# ============================================================
# 5. REVERSE ARITHMETIC METHODS
# ============================================================

class ReverseNumber:
    def __init__(self, value):
        self.value = value

    def __radd__(self, other):
        """Called for: normal_value + object"""
        return other + self.value

    def __rsub__(self, other):
        """Called for: normal_value - object"""
        return other - self.value

    def __rmul__(self, other):
        """Called for: normal_value * object"""
        return other * self.value

    def __rtruediv__(self, other):
        """Called for: normal_value / object"""
        return other / self.value


# Example:
# number = ReverseNumber(10)
# print(5 + number)
# print(20 - number)
# print(5 * number)
# print(100 / number)


# ============================================================
# 6. IN-PLACE OPERATOR METHODS
# ============================================================

class Score:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        """+="""
        self.value += other
        return self

    def __isub__(self, other):
        """-="""
        self.value -= other
        return self

    def __imul__(self, other):
        """*="""
        self.value *= other
        return self

    def __itruediv__(self, other):
        """/="""
        self.value /= other
        return self


# Example:
# score = Score(10)
# score += 5
# print(score.value)


# ============================================================
# 7. LENGTH AND CONTAINER METHODS
# ============================================================

class Team:
    def __init__(self, players):
        self.players = players

    def __len__(self):
        """Called by len(object)."""
        return len(self.players)

    def __getitem__(self, index):
        """Called by object[index]."""
        return self.players[index]

    def __setitem__(self, index, value):
        """Called by object[index] = value."""
        self.players[index] = value

    def __delitem__(self, index):
        """Called by del object[index]."""
        del self.players[index]

    def __contains__(self, player):
        """Called by player in object."""
        return player in self.players


# Example:
# team = Team(["Messi", "Ronaldo", "Neymar"])
# print(len(team))
# print(team[0])
# team[0] = "Mbappe"
# print("Neymar" in team)
# del team[2]


# ============================================================
# 8. ITERATION METHODS
# ============================================================

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        """Returns an iterator."""
        return self

    def __next__(self):
        """Returns the next value."""
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


# Example:
# for number in Counter(1, 5):
#     print(number)


# ============================================================
# 9. BOOLEAN BEHAVIOR
# ============================================================

class Account:
    def __init__(self, balance):
        self.balance = balance

    def __bool__(self):
        """Called by bool(object) and if object."""
        return self.balance > 0


# Example:
# account = Account(100)
# if account:
#     print("Account has money")


# ============================================================
# 10. CALLABLE OBJECT
# ============================================================

class Calculator:
    def __call__(self, a, b):
        """Allows an object to be called like a function."""
        return a + b


# Example:
# calculator = Calculator()
# print(calculator(10, 20))


# ============================================================
# 11. ATTRIBUTE ACCESS
# ============================================================

class PersonAttributes:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attribute):
        """Called when an attribute does not exist."""
        return f"{attribute} does not exist"

    def __setattr__(self, attribute, value):
        """Called whenever an attribute is assigned."""
        object.__setattr__(self, attribute, value)

    def __delattr__(self, attribute):
        """Called when an attribute is deleted."""
        object.__delattr__(self, attribute)


# Example:
# person = PersonAttributes("Nayamul")
# print(person.name)
# print(person.age)
# person.age = 25
# del person.age


# ============================================================
# 12. CONTEXT MANAGER: with
# ============================================================

class MyResource:
    def __enter__(self):
        """Called when entering a with block."""
        print("Resource opened")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Called when leaving a with block."""
        print("Resource closed")


# Example:
# with MyResource():
#     print("Using resource")


# ============================================================
# 13. HASHING
# ============================================================

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __hash__(self):
        """Returns a hash value for the object."""
        return hash(self.user_id)

    def __eq__(self, other):
        return self.user_id == other.user_id


# Example:
# user = User(101)
# users = {user}
# print(user in users)


# ============================================================
# 14. FORMAT
# ============================================================

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __format__(self, format_spec):
        """Controls format(object, spec)."""
        if format_spec == "price":
            return f"${self.price:.2f}"
        return f"{self.name}: {self.price}"


# Example:
# product = Product("Laptop", 75000)
# print(format(product, "price"))


# ============================================================
# 15. OTHER USEFUL MAGIC METHODS
# ============================================================

# __sizeof__()  -> Returns object's size reported by Python
# __dir__()     -> Controls the result of dir(object)
# __class__     -> Gives the object's class (attribute, not a method)
# __slots__     -> Restricts/stores instance attributes efficiently
#
# Example:
#
# class SmallObject:
#     __slots__ = ("name", "age")
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# ============================================================
# QUICK REFERENCE
# ============================================================

"""
Object / Lifecycle
------------------
__new__()       -> Creates an object
__init__()      -> Initializes an object
__del__()       -> Called when object is being destroyed

String / Representation
-----------------------
__str__()       -> print(object)
__repr__()      -> repr(object)
__format__()    -> format(object, spec)

Comparison
----------
__eq__()        -> ==
__ne__()        -> !=
__lt__()        -> <
__le__()        -> <=
__gt__()        -> >
__ge__()        -> >=

Arithmetic
----------
__add__()       -> +
__sub__()       -> -
__mul__()       -> *
__truediv__()   -> /
__floordiv__()  -> //
__mod__()       -> %
__pow__()       -> **

Reverse Arithmetic
------------------
__radd__()      -> right-side +
__rsub__()      -> right-side -
__rmul__()      -> right-side *
__rtruediv__()  -> right-side /

In-place Arithmetic
-------------------
__iadd__()      -> +=
__isub__()      -> -=
__imul__()      -> *=
__itruediv__()  -> /=

Containers
----------
__len__()       -> len(object)
__getitem__()   -> object[index]
__setitem__()   -> object[index] = value
__delitem__()   -> del object[index]
__contains__()  -> value in object

Iteration
---------
__iter__()      -> iter(object) / for loop
__next__()      -> next(iterator)

Other
-----
__bool__()      -> bool(object)
__call__()      -> object()
__getattr__()   -> Missing attribute access
__getattribute__() -> Attribute access
__setattr__()   -> Attribute assignment
__delattr__()   -> Attribute deletion
__enter__()     -> Enter a with block
__exit__()      -> Exit a with block
__hash__()      -> hash(object)
__sizeof__()    -> Object size
__dir__()       -> dir(object)

IMPORTANT:
----------
Magic methods are normally called indirectly by Python.

Examples:

    obj + other       -> obj.__add__(other)
    print(obj)        -> obj.__str__()
    len(obj)          -> obj.__len__()
    obj[0]            -> obj.__getitem__(0)
    value in obj      -> obj.__contains__(value)
    obj()             -> obj.__call__()
    with obj:         -> obj.__enter__() / obj.__exit__()
"""
