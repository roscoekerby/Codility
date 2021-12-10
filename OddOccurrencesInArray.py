def solution(A):
    B = A.copy()
    B.sort()
    
    if len(B) > 1:
        for i in range(len(B)-1):
            if B[i] != B[i+1] and i%2 ==0:
                return B[i]
            elif i == len(B)-2:
                return B[i+1]                
    else:
        return B[0]     
          
    
    
