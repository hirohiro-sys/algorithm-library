import bisect

N = int(input())
A = list(map(int,input().split()))

T = list(set(A))
T.sort()

B = [ None ] * N
for i in range(N):
    B[i] = bisect.bisect_left(T,A[i])
    B[i] += 1

Answer = [str(i) for i in B]
print(" ".join(Answer))

'''
座標圧縮
'''
