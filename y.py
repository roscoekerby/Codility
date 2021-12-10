def solution(A):
    A.sort()    
    i = 0
    
    if len(A) > 1:
        while (A[i] == A[i+1]):
            i = i+2
    else:
        return A[0]
    
    return A[i]
