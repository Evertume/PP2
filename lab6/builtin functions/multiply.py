# Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce
my_list = [1, -2, 4, -11]
def multiply(lst):
    return reduce(lambda x, y: x * y, lst)
print(multiply(my_list))