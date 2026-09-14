#File Reading and Writing in Python
#In Python, you can read and write files using built-in functions. The open() function is used to open a file and returns a file object. You can then use this object to read from or write to the file.

forRead=open("StudentForRead.txt", "r") # The "r" mode opens the file for reading. If the file does not exist, it will raise an error.
print("If readable return True:", forRead.readable()) # The readable() method checks if the file is readable and returns True if it is, otherwise it returns False.
print(forRead.read())
forRead.close()
print("\n-----------------\n")

forWrite=open("StudentForWrite.txt", "w") # The "w" mode opens the file for writing
print("If writable return True:", forWrite.writable()) # The writable() method checks if the file is writable and returns True if it is, otherwise it returns False.
forWrite.write("1004, Carol Williams, 19, carol.williams@example.com, Physics, 3.75, 2024")
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