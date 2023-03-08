# Write a Python program to copy the contents of a file to another file
source_file_path = input("Write the path of the source file: ") # C:\Users\dtbku\Documents\uni\second semester\PP2\somefile.txt
destination_file_path = input("Write the path of the destination file: ") # C:\Users\dtbku\Documents\uni\second semester\PP2\A.txt

# open the source file in read mode and the destination file in write mode
with open(source_file_path, "r") as source_file, open(destination_file_path, "w") as destination_file:
    content = source_file.read()
    destination_file.write(content)

print("content was copied successfully")