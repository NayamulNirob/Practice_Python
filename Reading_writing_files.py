#File Reading and Writing in Python
#In Python, you can read and write files using built-in functions. The open() function is used to open a file and returns a file object. You can then use this object to read from or write to the file.

forRead=open("StudentForRead.txt", "r") # The "r" mode opens the file for reading. If the file does not exist, it will raise an error.
readLines=forRead.readlines()
print("\nFile content:", readLines)
print("\nIf readable return True:", forRead.readable(),"\n") # The readable() method checks if the file is readable and returns True if it is, otherwise it returns False.
for line in readLines:
    print("Line: ", line.strip()) # The strip() method removes any leading and trailing whitespace characters (including newlines) from the string. This is useful for cleaning up the output when printing lines from a file.
forRead.close()

forRead=open("StudentForRead.txt", "r") # The "r" mode opens the file for reading. If the file does not exist, it will raise an error.
text=forRead.read()
print("\n",text)
size=len(text) # The len() function returns the number of characters in the string text, which is the content of the file. This gives us the size of the file in terms of the number of characters.
print("Size of the file is as Characters based: ", size)



forRead.close()
print("\n-----------------\n")

forWrite=open("StudentForWrite.txt", "w") # The "w" mode opens the file for writing
print("If writable return True:", forWrite.writable()) # The writable() method checks if the file is writable and returns True if it is, otherwise it returns False.
forWrite.write("1004, Carol Williams, 19, carol.williams@example.com, Physics, 3.75, 2024")
print("File written successfully.")
forWrite.close()
forWrite=open("StudentForWrite.txt", "a") # The "a" mode opens the file for writing without replacing the existing content. If the file does not exist, it will create a new file.
forWrite.write("\n1005, David Brown, 23, david.brown@example.com, Biology, 3.60, 2025")
print("File written successfully.")
forWrite.close()
print("\n-----------------\n")

forReadPlus=open("StudentForWrite.txt", "r+") # The "r+" mode opens the file for both reading and writing. If the file does not exist, it will raise an error.
print("If readable return True:", forReadPlus.readable())
print("If writable return True:", forReadPlus.writable())
print("File content:")
print(forReadPlus.read())
forReadPlus.close()
print("\n-----------------\n")

forCreateFile=open("Student.txt", "w") # The "w" mode opens the file for writing, replacing the existing content. If the file does not exist, it will create a new file.
forCreateFile.write("1006, Steven Byard, 27, steven.byard@example.com, Biology, 3.60, 2025")
print("File written successfully.")
forCreateFile.close()
print("\n-----------------\n")