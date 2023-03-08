# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path. import os
import os

path = "C:/Users/dtbku/Documents/uni"

# Check if path exists
if os.path.exists(path):
    directory, filename = os.path.split(path)
    print("Directory: ", directory)
    print("Filename: ", filename)
else:
    print("Path does not exists")