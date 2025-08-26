N = int(input())
D = int(input())

# 前日比の計算
A = [0] * (N+1)
for i in range(D):
    L, R = map(int, input().split())
    A[L] += 1
    if R + 1 <= N:
        A[R+1] -= 1

# 累積和を計算しつつ出力
ans = 0
for i in range(N):
    ans += A[i+1]
    print(ans)
  
"""問題URL
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g
"""
