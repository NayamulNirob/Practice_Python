# ============================================================
# Python List Practice
# ============================================================


# ------------------------------------------------------------
# 1. Create a List
# ------------------------------------------------------------

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)


# ------------------------------------------------------------
# 2. Access List Elements
# ------------------------------------------------------------

print("First fruit:", fruits[0])#Apple
print("Third fruit:", fruits[2])#Mango
print("Last fruit:", fruits[-1])#Orange


# ------------------------------------------------------------
# 3. Change a List Element
# ------------------------------------------------------------

fruits[1] = "Grapes"

print("After changing Banana to Grapes:", fruits)


# ------------------------------------------------------------
# 4. Add Elements Using append()
# ------------------------------------------------------------

fruits.append("Pineapple")

print("After append:", fruits) # now ["Apple", "Banana", "Mango", "Orange", "Pineapple"]


# ------------------------------------------------------------
# 5. Add Elements Using insert()
# ------------------------------------------------------------

fruits.insert(1, "Watermelon")

print("After insert:", fruits) # now ["Apple", "Watermelon", "Mango", "Orange", "Pineapple"]


# ------------------------------------------------------------
# 6. Remove an Element Using remove()
# ------------------------------------------------------------

fruits.remove("Mango")

print("After removing Mango:", fruits) # now ["Apple", "Watermelon", "Orange", "Pineapple"]


# ------------------------------------------------------------
# 7. Remove an Element Using pop()
# ------------------------------------------------------------

removed_fruit = fruits.pop(1)

print("Removed fruit:", removed_fruit) # Watermelon
print("After pop:", fruits) # ['Apple', 'Grapes', 'Orange', 'Pineapple']


# ------------------------------------------------------------
# 8. Find the Length of a List
# ------------------------------------------------------------

print("Number of fruits:", len(fruits)) # 4


# ------------------------------------------------------------
# 9. Loop Through a List
# ------------------------------------------------------------

print("\nAll fruits:")

for fruit in fruits:
    print(fruit)


# ------------------------------------------------------------
# 10. Create a List of Numbers
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print("\nNumbers:", numbers)


# ------------------------------------------------------------
# 11. Calculate the Sum of a List
# ------------------------------------------------------------

total = 0

for number in numbers: # [10, 20, 30, 40, 50] =Total: 150
    total = total + number

print("Total:", total)


# ------------------------------------------------------------
# 12. Find the Largest Number
# ------------------------------------------------------------

largest = numbers[0] # value index 0 =10

for number in numbers: #
    if number > largest:
        largest = number

print("Largest number:", largest)


# ------------------------------------------------------------
# 13. Find the Smallest Number
# ------------------------------------------------------------

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest number:", smallest)


# ------------------------------------------------------------
# 14. Find Even Numbers
# ------------------------------------------------------------

print("\nEven numbers:")

for number in numbers:
    if number % 2 == 0:
        print(number)


# ------------------------------------------------------------
# 15. Find Odd Numbers
# ------------------------------------------------------------

print("\nOdd numbers:")

for number in numbers:
    if number % 2 != 0:
        print(number)


# ------------------------------------------------------------
# 16. Check If an Element Exists
# ------------------------------------------------------------

search = "Mango"

if search in fruits:
    print("\n", search, "is found in the list.")
else:
    print("\n", search, "is not found in the list.")


# ------------------------------------------------------------
# 17. Sort a List in Ascending Order
# ------------------------------------------------------------

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print("\nAscending order:", numbers)


# ------------------------------------------------------------
# 18. Sort a List in Descending Order
# ------------------------------------------------------------

numbers.sort(reverse=True)

print("Descending order:", numbers)


# ------------------------------------------------------------
# 19. Reverse a List
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print("\nReversed list:", numbers)


# ------------------------------------------------------------
# 20. Count an Element
# ------------------------------------------------------------

numbers = [10, 20, 10, 30, 10, 40]

count = numbers.count(10)

print("\n10 appears", count, "times.")


# ------------------------------------------------------------
# 21. Find the Index of an Element
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

index = numbers.index(30)

print("Index of 30:", index)


# ------------------------------------------------------------
# 22. Copy a List
# ------------------------------------------------------------

original = [10, 20, 30]

copied = original.copy()

print("\nOriginal list:", original)
print("Copied list:", copied)


# ------------------------------------------------------------
# 23. Combine Two Lists
# ------------------------------------------------------------

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2

print("\nCombined list:", combined)


# ------------------------------------------------------------
# 24. Add All Elements of One List to Another
# ------------------------------------------------------------

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)

print("After extend:", list1)


# ------------------------------------------------------------
# 25. Remove All Elements Using clear()
# ------------------------------------------------------------

test_list = [10, 20, 30, 40]

test_list.clear()

print("\nAfter clear:", test_list)


# ------------------------------------------------------------
# 26. List Slicing
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print("\nFirst three elements:", numbers[0:3])
print("Elements from index 2:", numbers[2:])
print("Last two elements:", numbers[-2:])


# ------------------------------------------------------------
# 27. Loop With Index Using range()
# ------------------------------------------------------------

fruits = ["Apple", "Banana", "Mango"]

print("\nFruits with index:")

for i in range(len(fruits)):
    print(i, fruits[i])


# ------------------------------------------------------------
# 28. Count Even Numbers
# ------------------------------------------------------------

numbers = [10, 15, 20, 25, 30, 35, 40]

even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1

print("\nNumber of even numbers:", even_count)


# ------------------------------------------------------------
# 29. Create a List of Even Numbers
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("\nEven numbers list:", even_numbers)


# ------------------------------------------------------------
# 30. Create a List of Numbers Greater Than 50
# ------------------------------------------------------------

numbers = [25, 60, 45, 90, 30, 75, 10]

greater_than_50 = []

for number in numbers:
    if number > 50:
        greater_than_50.append(number)

print("\nNumbers greater than 50:", greater_than_50)


# ============================================================
# End of Python List Practice
# ============================================================