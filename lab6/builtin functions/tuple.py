# Write a Python program with builtin function that returns True if all elements of the tuple are true
def all_true(t):
    return all(t)
t1 = (True, True, True)
t2 = (True, False, True)
t3 = (False, False, False)

print(all_true(t1))
print(all_true(t2))
print(all_true(t3))