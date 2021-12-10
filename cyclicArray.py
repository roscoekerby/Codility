def solution(A, K):
    K = K % (len(A)-1)
    B = A[K-1:] + A[0:K-1]
    return B
