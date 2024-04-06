N,M = map(int,input().split())
G = [[] for _ in range(N)]
for i in range(M):
  a,b = map(int,input().split())
  G[a-1].append(b)
  G[b-1].append(a)

print(max(range(N), key=lambda x: len(G[x])) + 1)
"""別の出力の仕方
mx = max(friend)
ans = friend.index(mx)
print(ans + 1)
"""

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_eh
"""
