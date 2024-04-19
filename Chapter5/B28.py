n = int(input())
dp = [0] * (10**7+1)
dp[1] = 1
dp[2] = 1
for i in range(3,n+1):
  dp[i] = dp[i-1] + dp[i-2]
  dp[i] %=10**9+7
print(dp[n])

"""
https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ap
"""
