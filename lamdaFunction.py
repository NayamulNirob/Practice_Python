# This is a simple lambda function that calculates the expression a^2 + 2ab + b^2, which is the expansion of (a + b)^2.
# The structure of the lambda function is as follows:
# lambda arguments: expression
A_plus_B_Whole_Square = lambda a, b: a * a + 2 * a * b + b * b

print(A_plus_B_Whole_Square(3, 4))



print((lambda x: x * x * x)(2))