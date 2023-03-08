# Write a Python program to write a list to a file
path = input("Write the file path: ") # C:\Users\dtbku\Documents\uni\second semester\PP2\somefile.txt

list = ["potatoes", "beef", "onions", "eggs", "flour", "bay leaf"]

with open(path, "w") as file:
    for item in list:
        file.write(item +"\n")