import bisect
import sys

# 入力
N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

# それぞれ配列作成
P = []
for i in range(N):
    for j in range(N):
        P.append(A[i]+B[j])
    
Q = []
for i in range(N):
    for j in range(N):
        Q.append(C[i]+D[j])

Q.sort()

# 二分探索&出力
for i in range(len(P)):
    pos1 = bisect.bisect_left(Q,K-P[i])
    if pos1<N*N and Q[pos1]==K-P[i]:
        print("Yes")
        sys.exit(0)

print("No")
