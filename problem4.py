def solution(y): 
    string = [] 

    for x in range(1, y+1): 
        if x % 3 == 0 and x % 5 ==0: 
            string.append("FizzBuzz")    
        elif x % 3 == 0: 
            string.append("Fizz") 
        elif x % 5 == 0: 
            string.append("Buzz") 
        else: 
            string.append(str(x)) 
    return string 

y = 5
print(solution(y))
