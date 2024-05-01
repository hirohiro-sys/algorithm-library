Map = {}
for _ in range(int(input())):
  Query = input().split()
  if Query[0]=="1":
    Map[Query[1]]=Query[2]
  else:
    print(Map[Query[1]])

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bb
"""
