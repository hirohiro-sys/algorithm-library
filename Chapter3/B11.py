# 二分探索ライブラリ
import bisect

# 入力
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
X = [ None ] * Q
for i in range(Q):
    X[i] = int(input())

# 配列は昇順でないといけないためsort
A.sort()

for i in range(Q):
    # bisect_leftはX[i]がAの左から見て何番目に入るか
    ans = bisect.bisect_left(A,X[i])
    print(ans)
