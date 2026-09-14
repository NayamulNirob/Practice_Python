#Stack Practice LIFO
#Stack mainly use LIFO (Last In First Out) rule, so the last element will be removed first

books=[]
books.append("Learning Python")
books.append("Learn java")
books.append("Learn C++")
print("Books in the stack:",books)
books.pop() # for the rules of stack, the last element will be removed first
print("Books in the stack after popping:",books)

books.pop() # for the rules of stack, the last element will be removed first
print("Books in the stack after popping:",books)

books.pop() # for the rules of stack, the last element will be removed first
print("Books in the stack after popping:",books)

if not books:
    print("Stack is empty")
else:
    print("Stack is not empty")


#Queue practice
#Queue mainly use FIFO (First In First Out) rule, so the first element will be removed first
from collections import deque
bank = deque()
bank.append("Rahim")
bank.append("Karim")
bank.append("Abdul")
print("People in the queue:", bank)
bank.popleft() # for the rules of queue, the first element will be removed first
print("People in the queue after removing the first element:", bank)

bank.popleft() # for the rules of queue, the first element will be removed first
print("People in the queue after removing the first element:", bank)

bank.popleft() # for the rules of queue, the first element will be removed first
print("People in the queue after removing the first element:", bank)

if not bank:
    print("Queue is empty")
else:
    print("Queue is not empty")