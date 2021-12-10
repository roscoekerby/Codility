def solution(A):
    A.sort()    
    x = A[len(A)-1]
    for i in range(len(A)-1):
        if A[i] != A[i+1] and i%2 == 0:
            x = A[i]
        
    return x
