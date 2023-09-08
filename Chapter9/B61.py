# 入力
N, M = map(int, input().split())

# 友達の数を数える
friend = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
# インデックスは0から始まるから−１する
    friend[A-1] += 1
    friend[B-1] += 1

mx = max(friend)
ans = friend.index(mx)
# インデックスもどす
print(ans + 1)
