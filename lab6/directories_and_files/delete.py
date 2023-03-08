'''
Write a Python program to delete file by specified path. 
Before deleting check for access and whether a given path exists or not.
'''

import os

path = input("Write the path of the file to be deleted: ") # C:\Users\dtbku\Documents\uni\second semester\PP2\1.txt

if os.path.exists(path) and os.access(path, os.R_OK):
    os.remove(path)
    print("File deleted successfully")
else:
    print("File does not exist or it does not accessible")