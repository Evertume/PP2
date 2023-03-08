# Write a Python program to count the number of lines in a text file
import os
line_cnt = 0
path = input("Write the file path: ") # C:\Users\dtbku\Documents\uni\second semester\PP2\somefile.txt
# open it and count the number of lines
with open(path, "r") as file:
    for line in file:
        line_cnt +=1

print("Number of lines:", line_cnt)