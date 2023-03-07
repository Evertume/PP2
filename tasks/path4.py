'''
You need to modify the program from the second task.
You need to ask which line do youwant to change, in the prompt you can write a new line, which will replace the old one.
You need to stop the process if user entered triple asterisk “***”.
After that you need to save the file with new content.
'''

import os

path = input("Write directory path: ")

filename = input("Write a name of the file: ")

file_path = os.path.join(path, filename)

if not os.path.exists(file_path):
    print (file_path, "does not exist.")
    exit()

with open(file_path, "r") as f:
    content = f.read()

print (content)
n ="/"
lines = []
with open(file_path, "r") as f:
    lines = f.readlines()
    while n != "***":
        try:
            n = int(n)
            if n < len(lines):
                lines[n] = input() + "\n"
            else:
                print("wrong lines")
        except ValueError:
        # Handle the exception
            print('Please enter an integer')
        n=input("Write line number:")
with open(file_path[:-3]+"5"+".py", 'a') as f:
    f.writelines(lines)