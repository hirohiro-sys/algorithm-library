N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
K = int(input())
query = [list(map(int,input().split())) for _ in range(K)]

prefix_sum = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        prefix_sum[i+1][j+1] = prefix_sum[i+1][j] + A[i][j]
for j in range(M):
    for i in range(N):
        prefix_sum[i+1][j+1] = prefix_sum[i][j+1] + prefix_sum[i+1][j+1]

for i,j,x,y in query:
    print(prefix_sum[i-1][j-1]+prefix_sum[x][y] - prefix_sum[i-1][y]-prefix_sum[x][j-1])

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h
"""
