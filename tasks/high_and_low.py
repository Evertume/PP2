s = str(input())
numbers = s.split()
def high_and_low(numbers):
    s = sorted(numbers)
    return (s[-1] + " " + s[0])
print(high_and_low(numbers))