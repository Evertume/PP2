def XO(s):
    x_count, o_count = 0, 0
    
    for i in s:
        if i == 'x' or i == 'X':
            x_count += 1
            
        elif i == 'o' or i == 'O':
            o_count += 1
            
    if x_count == o_count:
        s = True
    else:
        s = False
    
    return s
    
print(XO(input()))