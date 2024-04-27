N = int(input())
H = list(map(int, input().split()))

dp = [0] * N
# インデックスがごちゃごちゃになるのを防ぐため0から埋める
dp[0] = 0
dp[1] = abs(H[0] - H[1])
for i in range(2, N):
	# i+1する場合とi+2する場合でどちらが小さいか
	dp[i] = min(dp[i-1] + abs(H[i-1]-H[i]), dp[i-2] + abs(H[i-2]-H[i]))

print(dp[-1]) #dp[n-1]

"""
https://atcoder.jp/contests/tessoku-book/tasks/dp_a
"""
