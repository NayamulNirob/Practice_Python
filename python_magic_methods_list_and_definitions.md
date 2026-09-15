# Python Magic Methods (Dunder Methods)

Magic methods, also called **dunder methods**, are special methods in Python whose names begin and end with double underscores, such as `__init__()` and `__str__()`.

Python calls these methods automatically in response to certain operations, functions, operators, or syntax.

---

## 1. Object Creation and Lifecycle

| Magic Method | Definition | Example / Trigger |
|---|---|---|
| `__new__()` | Creates and returns a new instance of a class. It runs before `__init__()`. | `obj = MyClass()` |
| `__init__()` | Initializes an object after it has been created. | `MyClass()` |
| `__del__()` | Called when an object is being destroyed. | Object cleanup |

### `__new__()`

Used when you need to control how an object is created.

```python
class Person:
    def __new__(cls, name):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
```

### `__init__()`

Used to initialize instance attributes.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

# 2. String Representation

| Magic Method | Definition | Trigger |
|---|---|---|
| `__str__()` | Returns a human-readable string representation of an object. | `print(obj)`, `str(obj)` |
| `__repr__()` | Returns a developer-oriented representation of an object. | `repr(obj)` |
| `__format__()` | Controls how an object is formatted. | `format(obj)` |

### `__str__()`

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"


student = Student("Nayamul")
print(student)
```

Output:

```text
Student: Nayamul
```

### `__repr__()`

```python
class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student({self.name!r})"
```

Useful for debugging and inspecting objects.

---

# 3. Comparison Magic Methods

These methods allow custom objects to work with comparison operators.

| Magic Method | Operator | Definition |
|---|---:|---|
| `__eq__()` | `==` | Checks whether two objects are equal. |
| `__ne__()` | `!=` | Checks whether two objects are not equal. |
| `__lt__()` | `<` | Checks whether one object is less than another. |
| `__le__()` | `<=` | Checks whether one object is less than or equal to another. |
| `__gt__()` | `>` | Checks whether one object is greater than another. |
| `__ge__()` | `>=` | Checks whether one object is greater than or equal to another. |

### Example

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


a = Number(10)
b = Number(20)

print(a == b)
print(a < b)
```

Output:

```text
False
True
```

---

# 4. Arithmetic Magic Methods

These methods allow custom objects to work with arithmetic operators.

| Magic Method | Operator | Definition |
|---|---:|---|
| `__add__()` | `+` | Defines addition. |
| `__sub__()` | `-` | Defines subtraction. |
| `__mul__()` | `*` | Defines multiplication. |
| `__truediv__()` | `/` | Defines true division. |
| `__floordiv__()` | `//` | Defines floor division. |
| `__mod__()` | `%` | Defines modulo/remainder. |
| `__pow__()` | `**` | Defines exponentiation. |
| `__matmul__()` | `@` | Defines matrix multiplication. |
| `__neg__()` | `-obj` | Defines unary negative. |
| `__pos__()` | `+obj` | Defines unary positive. |
| `__abs__()` | `abs(obj)` | Defines absolute value. |

### Example

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)


a = Number(10)
b = Number(20)

print(a + b)
```

Output:

```text
30
```

`a + b` effectively invokes:

```python
a.__add__(b)
```

---

# 5. Reverse Arithmetic Methods

Reverse arithmetic methods are used when your custom object appears on the **right-hand side** of an operator.

| Magic Method | Operator | Definition |
|---|---:|---|
| `__radd__()` | `+` | Handles right-side addition. |
| `__rsub__()` | `-` | Handles right-side subtraction. |
| `__rmul__()` | `*` | Handles right-side multiplication. |
| `__rtruediv__()` | `/` | Handles right-side true division. |
| `__rfloordiv__()` | `//` | Handles right-side floor division. |
| `__rmod__()` | `%` | Handles right-side modulo. |
| `__rpow__()` | `**` | Handles right-side exponentiation. |
| `__rmatmul__()` | `@` | Handles right-side matrix multiplication. |

### Example

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __radd__(self, other):
        return other + self.value


number = Number(10)

print(5 + number)
```

Output:

```text
15
```

---

# 6. In-Place Arithmetic Methods

These methods define behavior for operators such as `+=`, `-=`, and `*=`.

| Magic Method | Operator | Definition |
|---|---:|---|
| `__iadd__()` | `+=` | Defines in-place addition. |
| `__isub__()` | `-=` | Defines in-place subtraction. |
| `__imul__()` | `*=` | Defines in-place multiplication. |
| `__itruediv__()` | `/=` | Defines in-place true division. |
| `__ifloordiv__()` | `//=` | Defines in-place floor division. |
| `__imod__()` | `%=` | Defines in-place modulo. |
| `__ipow__()` | `**=` | Defines in-place exponentiation. |
| `__imatmul__()` | `@=` | Defines in-place matrix multiplication. |

### Example

```python
class Score:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, amount):
        self.value += amount
        return self


score = Score(10)
score += 5

print(score.value)
```

Output:

```text
15
```

---

# 7. Container and Sequence Methods

These methods allow an object to behave like a list, tuple, or other container.

| Magic Method | Definition | Trigger |
|---|---|---|
| `__len__()` | Returns the number of items. | `len(obj)` |
| `__getitem__()` | Gets an item by index or key. | `obj[index]` |
| `__setitem__()` | Sets an item by index or key. | `obj[index] = value` |
| `__delitem__()` | Deletes an item. | `del obj[index]` |
| `__contains__()` | Checks whether a value exists. | `value in obj` |
| `__missing__()` | Provides behavior for a missing dictionary key. | `obj[key]` |

### Example

```python
class Team:
    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)

    def __getitem__(self, index):
        return self.players[index]

    def __contains__(self, player):
        return player in self.players


team = Team(["Messi", "Ronaldo", "Neymar"])

print(len(team))
print(team[0])
print("Messi" in team)
```

Output:

```text
3
Messi
True
```

---

# 8. Iteration Methods

| Magic Method | Definition | Trigger |
|---|---|---|
| `__iter__()` | Returns an iterator for the object. | `iter(obj)`, `for` loop |
| `__next__()` | Returns the next item from an iterator. | `next(obj)` |

### Example

```python
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


for number in Counter(1, 5):
    print(number)
```

Output:

```text
1
2
3
4
5
```

---

# 9. Boolean and Truth-Value Methods

| Magic Method | Definition | Trigger |
|---|---|---|
| `__bool__()` | Defines whether an object is considered `True` or `False`. | `bool(obj)`, `if obj` |

### Example

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def __bool__(self):
        return self.balance > 0


account = Account(100)

if account:
    print("Account has money")
```

---

# 10. Callable Objects

| Magic Method | Definition | Trigger |
|---|---|---|
| `__call__()` | Allows an object to be called like a function. | `obj()` |

### Example

```python
class Calculator:
    def __call__(self, a, b):
        return a + b


calculator = Calculator()

print(calculator(10, 20))
```

Output:

```text
30
```

Without `__call__()`, `calculator(10, 20)` would normally raise a `TypeError`.

---

# 11. Attribute Access Methods

| Magic Method | Definition |
|---|---|
| `__getattr__()` | Called when normal attribute lookup cannot find an attribute. |
| `__getattribute__()` | Called for almost every attribute access. |
| `__setattr__()` | Called when assigning an attribute. |
| `__delattr__()` | Called when deleting an attribute. |

### `__getattr__()` Example

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attribute):
        return f"{attribute} does not exist"


person = Person("Nayamul")

print(person.age)
```

Output:

```text
age does not exist
```

---

# 12. Context Manager Methods

These methods are used with the `with` statement.

| Magic Method | Definition | Trigger |
|---|---|---|
| `__enter__()` | Runs when entering a `with` block. | `with obj:` |
| `__exit__()` | Runs when leaving a `with` block. | End of `with` |

### Example

```python
class Resource:
    def __enter__(self):
        print("Resource opened")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource closed")


with Resource():
    print("Using resource")
```

Output:

```text
Resource opened
Using resource
Resource closed
```

A common real-world example is:

```python
with open("file.txt") as file:
    data = file.read()
```

---

# 13. Hashing and Equality

| Magic Method | Definition | Trigger |
|---|---|---|
| `__hash__()` | Returns a hash value for an object. | `hash(obj)` |
| `__eq__()` | Determines equality between objects. | `obj1 == obj2` |

Hashing is important when objects are used in:

- `set`
- Dictionary keys
- Other hash-based collections

### Example

```python
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __hash__(self):
        return hash(self.user_id)

    def __eq__(self, other):
        return self.user_id == other.user_id


user = User(101)

users = {user}

print(user in users)
```

---

# 14. Descriptor Methods

Descriptors are advanced Python features used heavily by frameworks and libraries.

| Magic Method | Definition |
|---|---|
| `__get__()` | Controls how an attribute is retrieved. |
| `__set__()` | Controls how an attribute is assigned. |
| `__delete__()` | Controls how an attribute is deleted. |
| `__set_name__()` | Receives the name assigned to a descriptor during class creation. |

### Simple Example

```python
class Descriptor:
    def __get__(self, instance, owner):
        return "Value retrieved"

    def __set__(self, instance, value):
        print(f"Value assigned: {value}")


class Person:
    name = Descriptor()


person = Person()

print(person.name)
person.name = "Nayamul"
```

Descriptors are commonly encountered when learning `property`, ORM systems, and framework internals.

---

# 15. Class Creation Methods

These are more advanced methods related to class creation.

| Magic Method | Definition |
|---|---|
| `__init_subclass__()` | Runs when a class is subclassed. |
| `__class_getitem__()` | Controls subscription of a class, such as `MyClass[int]`. |
| `__prepare__()` | Used by metaclasses to prepare the namespace before a class body executes. |
| `__instancecheck__()` | Customizes `isinstance()`. |
| `__subclasscheck__()` | Customizes `issubclass()`. |

### `__init_subclass__()` Example

```python
class Parent:
    def __init_subclass__(cls):
        print(f"{cls.__name__} was created")


class Child(Parent):
    pass
```

Output:

```text
Child was created
```

---

# 16. Formatting and Representation

| Magic Method | Definition | Trigger |
|---|---|---|
| `__format__()` | Controls custom formatting. | `format(obj, spec)` |
| `__bytes__()` | Defines conversion of an object to `bytes`. | `bytes(obj)` |
| `__fspath__()` | Allows an object to represent a filesystem path. | `os.fspath(obj)` |

### `__format__()` Example

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __format__(self, spec):
        if spec == "price":
            return f"${self.price:.2f}"

        return self.name


product = Product("Laptop", 75000)

print(format(product, "price"))
```

---

# 17. Numeric Conversion Methods

| Magic Method | Definition | Trigger |
|---|---|---|
| `__int__()` | Converts an object to an integer. | `int(obj)` |
| `__float__()` | Converts an object to a float. | `float(obj)` |
| `__complex__()` | Converts an object to a complex number. | `complex(obj)` |
| `__index__()` | Provides an integer representation for contexts requiring an exact integer. | Indexing and some integer operations |
| `__round__()` | Defines behavior for `round()`. | `round(obj)` |
| `__trunc__()` | Defines truncation. | `math.trunc(obj)` |
| `__floor__()` | Defines floor operation. | `math.floor(obj)` |
| `__ceil__()` | Defines ceiling operation. | `math.ceil(obj)` |

### Example

```python
class Price:
    def __init__(self, value):
        self.value = value

    def __float__(self):
        return float(self.value)


price = Price(99)

print(float(price))
```

---

# 18. Bitwise Operators

| Magic Method | Operator | Definition |
|---|---:|---|
| `__and__()` | `&` | Bitwise AND |
| `__or__()` | `|` | Bitwise OR |
| `__xor__()` | `^` | Bitwise XOR |
| `__invert__()` | `~` | Bitwise inversion |
| `__lshift__()` | `<<` | Left shift |
| `__rshift__()` | `>>` | Right shift |

There are also reverse and in-place versions such as:

```text
__rand__()
__ror__()
__rxor__()
__rlshift__()
__rrshift__()

__iand__()
__ior__()
__ixor__()
__ilshift__()
__irshift__()
```

---

# 19. Async Magic Methods

Python's asynchronous programming uses special methods for `async for` and `async with`.

| Magic Method | Definition |
|---|---|
| `__aiter__()` | Returns an asynchronous iterator. |
| `__anext__()` | Returns the next asynchronous value. |
| `__aenter__()` | Runs when entering `async with`. |
| `__aexit__()` | Runs when leaving `async with`. |

### Example

```python
class AsyncResource:
    async def __aenter__(self):
        print("Async resource opened")
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        print("Async resource closed")
```

Used with:

```python
async with AsyncResource():
    pass
```

---

# 20. Pickling and Serialization Methods

| Magic Method | Definition |
|---|---|
| `__getstate__()` | Defines what object state should be serialized. |
| `__setstate__()` | Restores object state during deserialization. |
| `__reduce__()` | Provides information needed to reconstruct an object. |
| `__reduce_ex__()` | Extended version of `__reduce__()`. |

These methods are commonly relevant when using Python's `pickle` module.

---

# 21. Other Useful Magic Methods

| Magic Method | Definition |
|---|---|
| `__sizeof__()` | Returns the object's size as reported by Python. |
| `__dir__()` | Controls the result of `dir(obj)`. |
| `__copy__()` | Controls shallow copying. |
| `__deepcopy__()` | Controls deep copying. |

---

# Quick Reference

## Most Important Magic Methods for Beginners

```text
__init__()          -> Initialize an object
__str__()           -> User-friendly string
__repr__()          -> Developer/debug representation

__eq__()            -> ==
__ne__()            -> !=
__lt__()            -> <
__le__()            -> <=
__gt__()            -> >
__ge__()            -> >=

__add__()           -> +
__sub__()           -> -
__mul__()           -> *
__truediv__()       -> /
__floordiv__()      -> //
__mod__()           -> %
__pow__()           -> **

__len__()           -> len(obj)
__getitem__()       -> obj[index]
__setitem__()       -> obj[index] = value
__delitem__()       -> del obj[index]
__contains__()      -> value in obj

__iter__()          -> Iteration / for loop
__next__()          -> next(obj)

__bool__()          -> bool(obj)
__call__()          -> obj()

__enter__()         -> Enter with block
__exit__()          -> Exit with block

__getattr__()       -> Missing attribute
__setattr__()       -> Attribute assignment
__delattr__()       -> Attribute deletion

__hash__()          -> hash(obj)
__format__()        -> format(obj)
```

---

# How Python Syntax Maps to Magic Methods

One of the easiest ways to understand magic methods is to see what Python calls behind common syntax.

```python
obj + other
# roughly -> obj.__add__(other)

obj - other
# roughly -> obj.__sub__(other)

obj * other
# roughly -> obj.__mul__(other)

obj == other
# roughly -> obj.__eq__(other)

obj < other
# roughly -> obj.__lt__(other)

print(obj)
# roughly -> obj.__str__()

len(obj)
# roughly -> obj.__len__()

obj[0]
# roughly -> obj.__getitem__(0)

obj[0] = value
# roughly -> obj.__setitem__(0, value)

del obj[0]
# roughly -> obj.__delitem__(0)

value in obj
# roughly -> obj.__contains__(value)

for item in obj:
    ...
# uses __iter__() and __next__()

bool(obj)
# roughly -> obj.__bool__()

obj()
# roughly -> obj.__call__()

with obj:
    ...
# uses __enter__() and __exit__()
```

---

# Recommended Learning Order

If you are learning Python OOP, focus on these first:

1. `__init__()`
2. `__str__()`
3. `__repr__()`
4. `__eq__()`
5. `__lt__()` / `__gt__()`
6. `__add__()`
7. `__len__()`
8. `__getitem__()`
9. `__iter__()` / `__next__()`
10. `__contains__()`
11. `__bool__()`
12. `__call__()`
13. `__enter__()` / `__exit__()`
14. `__getattr__()` / `__setattr__()`
15. `__new__()` and advanced methods

> **Key idea:** Magic methods make your custom Python classes behave like Python's built-in objects.
