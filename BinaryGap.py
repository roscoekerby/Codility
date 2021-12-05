#Find longest sequence of zeros in binary representation of an integer.
def solution(N):    
    binary = bin(N)[2:]
    longestBinaryGap = 0
    newGap = 0
    i = 0
    
    while i < len(binary)-1:
        if binary[i] == '1' and binary[i+1] == '0':            
            newGap = 1
            x = i+1
            
            while x < len(binary)-1:
                x = x+1
                
                if (binary[x] == '0'):
                    newGap = newGap+1                    
                elif (binary[x] == '1'):
                    newGap = newGap
                    
                    if (longestBinaryGap < newGap):
                        longestBinaryGap = newGap                        
                        newGap = 1                        
                    break
        i = i+1

    return longestBinaryGap
