def solution(A, K):
    Anew = A
    lenA = len(A)
    
    if lenA > 0:
        for i in range(K):
            Alast = Anew[lenA-1]
            Anew = Anew[0:lenA-1]
            Anew.insert(0, Alast)
    else:
        Anew = []
        
    return Anew
