def process(a, b):
    x = a.split(" ")
    ans = []
    for i in x:
        if i.isnumeric():
            if i>b:
                ans.append(i)
        else:
            if i.startswith(b):
                ans.append(i)
    return ans
print(process("the weather is great today", "t"))
print(process("92 86 93", "90"))