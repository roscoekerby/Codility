def solution(A, K):
    Anew = A
    lenA = len(A)
    
    for i in range(K):
        Alast = Anew[lenA-1]
        Anew = Anew[0:lenA-1]
        Anew.insert(0, Alast)
        
    return Anew
