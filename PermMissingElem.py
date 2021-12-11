def solution(A):
    lenA = len(A)
    
    if lenA > 2:
        B = A.copy()    
        B.sort()       
        xlast = B[0]
        
        for x in B[1:]:           
            if x != xlast+1:
                return xlast+1
            xlast = x
    
    elif lenA == 1:
        if A == [1]:
            return 2
        if A == [2]:
            return 1
    elif A == []:
        return 1
    elif lenA == 2:
        if A == [1,2]:
            return 3
        if A == [1,3]:
            return 2       
        if A == [2,3]:
            return 1
        if A == [2,1]:
            return 3
        if A == [3,1]:
            return 2
        if A == [3,2]:
            return 1

    if B.count(1) == 0:
        return 1

    if B.count(lenA+1) == 0:
        return lenA+1
