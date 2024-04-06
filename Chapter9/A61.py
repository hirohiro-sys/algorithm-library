N,M = map(int,input().split())
G = [[] for _ in range(N)]

for i in range(M):
  a,b = map(int,input().split())
  G[a-1].append(b)
  G[b-1].append(a)

for i in range(N):
  print(str(i+1)+':',set(G[i]) if len(G[i]) != 0 else '{}') 

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bi
"""
