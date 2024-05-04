n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))

p = []
for i in a:
  for j in b:
    p.append(i+j)
q = []
for i in c:
  for j in d:
    q.append(i+j)

p = set(p)
q = set(q)

for i in p:
  if k-i in q:
    print("Yes")
    exit()
print("No")

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_n
"""
