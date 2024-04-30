from collections import deque

n,m = map(int,input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  G[a].append(b)
  G[b].append(a)


queue = deque()
queue.append(1)
dist = [-1] * (n+1)
dist[1] = 0
while queue:
  pos = queue.popleft()
  for i in G[pos]:
    if dist[i]==-1:
      dist[i] = dist[pos] + 1
      queue.append(i)

for i in range(1,n+1):
  print(dist[i])


"""
https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_an
"""
