# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os

path = input("Write directory path: ") # C:\Users\dtbku\Documents\uni\second semester\PP2

for letter in range(65, 91):
    filepath = os.path.join(path, chr(letter) + ".txt")
    with open(filepath, "w") as file:
        file.write("This is file " + chr(letter))