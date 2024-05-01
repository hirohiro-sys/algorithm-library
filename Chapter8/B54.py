a = [int(input()) for _ in range(int(input()))]
Map = {}
ans = 0
for i in a:
  ans += Map.get(i,0)
  Map[i] = Map.get(i,0) + 1
print(ans)

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ea
"""
