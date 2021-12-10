def solution(A):
    A.sort()    
    i = 0
    
    while (A[i] == A[i+1]):
        i = i +1
    
    return A[i+1]
