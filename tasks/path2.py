'''
You need to add extra functionality to the program from the first task.
User will be prompted to enter the name of the file and you need to print:
    the data in the file on the screen 
    how many characters in the file
    how many function definitions
    how many equal signs
'''

import os

path = input("Write directory path: ")

filename = input("Write a name of the file: ")

file_path = os.path.join(path, filename)

if not os.path.exists(file_path):
    print (file_path, "does not exist.")
    exit()

# print the data in the file on the screen 

with open(file_path, "r") as f:
    content = f.read()

print (content)

# print how many characters in the file

number_of_characters = len(content)
print("Number of characters in the file = ", number_of_characters)

# print how many function definitions

number_of_functions = content.count("def ")
print("Number of function defenitions = ", number_of_functions)

# print how many equal signs

number_of_equal_signs = content.count("=")
print("Number of equal signs = ", number_of_equal_signs)