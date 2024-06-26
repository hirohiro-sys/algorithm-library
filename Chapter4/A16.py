N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dp = [0] * 100001
dp[1] = 0
dp[2] = A[0]
for i in range(3,N+1):
  dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])
print(dp[N])

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p
"""
