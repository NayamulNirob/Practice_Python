#Recursion can call itself to solve a problem. It is a powerful technique that can be used to solve complex problems by breaking them down into smaller, more manageable subproblems. Recursion is often used in algorithms and data structures, such as tree traversal, sorting, and searching.
#In this example, we have a simple recursive function that calculates the factorial of a number.
# Factorial of a number n is the product of all positive integers less than or equal to n. It is denoted by n! and is defined as:
# n! = n * (n-1)! For Factorial of n number recursion is used to calculate the factorial of n-1 until it reaches the base case of 0! = 1. The function then multiplies the results of each recursive call to calculate the final factorial value.

def factorial(n):
    if  n == 0:
        return 1
    elif n<0:
        return "Factorial is not defined for negative numbers"
    else:
        return n * factorial(n - 1) # function calls itself with n-1 until it reaches the base case of 0! = 1. The function then multiplies the results of each recursive call to calculate the final factorial value.

print(factorial(5)) # Output: for 5 = 5 * 4 * 3 * 2 * 1 = 120  n!=n*(n-1)!