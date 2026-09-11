#Match case statement in python

Day=input("Enter a day : ")
# fullweek=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

match Day:
    case "Monday":
        print("Workday 1")
    case "Tuesday":
        print("Workday 2")
    case "Wednesday":
        print("Workday 3")
    case "Thursday":
        print("Workday 4")
    case "Friday":
        print("Workday 5")
    case "Saturday":
        print("Weekend 1")
    case "Sunday":
        print("Weekend 2")
    case _:
        print("input a valid day")

#marks calculation using match case
result=float(input("Enter your total marks: "))

match result:
    case result if  result > 100 or result < 0: # In Python match-case, _ is a wildcard pattern. and result is a variable that can be used to capture the value of the matched case.
        print("Invalid marks")
    case _ if result >= 90: # In Python match-case, _ is a wildcard pattern.
        print("Golden A+")
    case _ if result >= 80:
        print("A+")
    case _ if result >= 70:
        print("A")
    case _ if result >= 60:
        print("A-")
    case _ if result >= 50:
        print("B")
    case _ if result >= 40:
        print("B-")
    case _ if result >= 30:
        print("C")
    case _:
        print("Fail")

#While loop with break and continue statement
start =int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

sumOfEven = 0
sumOfOdd = 0

while start <= end:
    if start % 2 == 0:
        sumOfEven += start
        print("Even number is:", start)
        start += 1
        continue

    if start % 2 !=  0:
        sumOfOdd += start
        print("Odd number is:", start)
        start += 1
        continue

    if start == end:
        print("End number is:", start)
        break

    start += 1

print("While loop with break and continue statement")
print("Sum of even numbers:", sumOfEven)
print("Sum of odd numbers:", sumOfOdd)