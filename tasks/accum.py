def accum(text):
    str_holder = text.lower().strip()
    answer = ''
    
    counter = 0
    
    for x in str_holder:
        if counter == 0:
            
            opt1 = x.upper()
            answer += opt1
            
            
        else:
            opt2 = (str("-" + x.upper() + str(x*counter)))
            answer += opt2
        counter += 1
        

    return answer
print(accum(input()))