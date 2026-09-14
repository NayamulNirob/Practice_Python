#Matrix or 2D array example
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
print(matrix[0][1])
print(matrix[1][1])
print(matrix[2][1])

for row in matrix:
    for col in row:
        print(col, end=" ")


#Set Example
setPractice = {1, 2, 3, 4, 5, 6, 7, 8, 9}

num2=set(setPractice)
num2.add(10)
num2.remove(1)
print('set Example: ',num2)

#Dictionary Example
dictPractice = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
print(dictPractice)
print(dictPractice[1])
print(dictPractice.get(4))


#Tuple Example
tuplePractice = ('Must', 'Have to', 'Ought to', 'Should to','Shall to', 'Will to', 'Would to', 'Can to', 'Could to', 'May to', 'Might to')
tuplePractice2=(
(101,'John Doe'),
(102,'Jane Smith'),
(103,'Alice Johnson'),
(104,'Bob Brown'),
(105,'Charlie Davis')
)
print(tuplePractice)
print(tuplePractice[2])

print(tuplePractice2)
print(tuplePractice2[1][1]) 