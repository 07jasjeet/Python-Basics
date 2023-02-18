import os

# Get location of this python script
print(f"Location of this file using __file__: {os.path.dirname(__file__)}")
print(f"Location of this file using os.getcwd(): {os.getcwd()}")
# os.getcwd() gives us the file path that is selected in the terminal.
# Try changing it using 'cd basics' and back by 'cd ..'.

# Visit https://www.w3schools.com/python/python_file_write.asp

f = open("F:\\Python Programming\\Basics\\test.txt", "w")
f.write("Hello world")
f.close

f = open("F:\\Python Programming\\Basics\\test.txt", "r")
print(f.read())

print(f.read())     # Results in empty read.

# A cursor defines where we are reading from, always set cursor before reading.
f.seek(0)   
print(f.read())
f.close

# Use with to open and close file automatically.
with open("F:\\Python Programming\\Basics\\test.txt") as file:
    print(f"File read using with:\n {file.read()}")

# Discover multiple modes for file interaction.
