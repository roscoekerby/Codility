def solution(A):
    count = 0
    count2 = 0
    sumArray = []
    min1  = 10000
    i = 0
    
    for x in A:
        count = count + x
        sumArray.append(count)
        
    for y in A:
        count2 = count2 + y        

        if i < len(A)-1:
            if min1 > abs(count2-(sumArray[len(A)-1] - count2)):
                min1 = abs(count2-(sumArray[len(A)-1] - count2))
    
        i = i+1
    
    return min1
