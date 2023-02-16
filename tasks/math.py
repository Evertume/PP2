import math
def function(n):
    if math.sqrt(n)%2==0 or math.sqrt(n)%2==1:
        print(int((math.sqrt (n)+1)**2))
    else:
        print("-1")
print(function(121))