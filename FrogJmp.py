import math

def solution(X, Y, D):
    delta = Y-X
    ceil = math.ceil(delta/D)
    
    return ceil
