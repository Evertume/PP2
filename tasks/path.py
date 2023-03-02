#Your program needs to accept a certain path from the prompt and show a list of python files in that directory

import os
import glob

path = input("Write directory path: ")

search_path = os.path.join(path, "*.py")

py_files = glob.glob(search_path)

print("Python files in directory:")
for file in py_files:
    print(file)
