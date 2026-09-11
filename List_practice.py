text= input("Enter the string: ")

# numberOfWords = len(text.split())
# numberOfLines = len(text.split("\n"))
# numberOfCharacters = len(text)
# numberOfDigits = len(list(filter(str.isdigit, text)))

numberOfCharacters = 0
numberOfWords = 0
numberOfDigits = 0

for x in text:
    x=x.lower()
    if 'a' < x < 'z':
        numberOfCharacters+=1
    if '0' <= x <= '9':
        numberOfDigits+=1
    if x==' ':
        numberOfWords+=1

print(f"The number of characters in the string is: {numberOfCharacters}")
print(f"The number of words in the string is: {numberOfWords+1}")
# print(f"The number of lines in the string is: {numberOfLines}")
print(f"The number of digits in the string is: {numberOfDigits}")