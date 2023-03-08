# Write a Python program that invoke square root function after specific milliseconds. Sample Input: 25100 2123 Sample Output: Square root of 25100 after 2123 miliseconds is 158.42979517754858
import time
import math

string = input()
number, delay = map(int, string.split()) # splits the string by a space and converts to integers using map

time.sleep(delay / 1000) # convert to seconds

sqrt = math.sqrt(number)

print(f"Square root of {number} after {delay} miliseconds is {sqrt}")