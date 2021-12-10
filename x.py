def solution(A):
    A.sort()    
    x = 0
    for i in range(len(A)-1):
        if A[i] != A[i+1] and i%2 == 0:
            x = i
        
    return A[x]
