#Matrix or 2D array example
import numpy as np
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


#Reshape is used to divide an array with numpy
x=np.array([1,2,3,4,5,6,7,8,9,10])
new=x.reshape((2,5))
print(new)


#With the help of numpy.reshape we can convert multidimensional array into single array

multi=np.array([[1,2,3,4,5],[5,6,7,8,9]])
single=multi.reshape(-1)
print(single)

arr=np.array([[[9,2,3],[4,8,6],[6,8,9]]])

# for x in arr:
#     for y in x:
#       for  z in y:
#         print(z)

for x in np.nditer(arr): #same thing as for with built-in numpy
    print(x)