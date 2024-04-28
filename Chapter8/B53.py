import heapq

# 仕事を登録
G = [[] for _ in range(2001)]
N,D = map(int,input().split())
for _ in range(N):
  X,Y = map(int,input().split())
  G[X].append(Y)
  
  
# 優先度付きキューでマイナスを指定して最大値を取る
Q = []
Answer = 0
for i in range(1,D + 1):
  for y in G[i]:
    heapq.heappush(Q,-y)
  if Q:
    Answer -= heapq.heappop(Q)
  
print(Answer)


"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dl
"""
