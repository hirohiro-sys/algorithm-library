n,k = map(int,input().split())
a = list(map(int,input().split()))

n = n//2
a_before = a[:n]
a_after = a[n:]

b_before = set([0])
for i in a_before:
  for j in list(b_before):
    b_before.add(i+j)
    
b_after = set([0])
for i in a_after:
  for j in list(b_after):
    b_after.add(i+j)

for i in b_before:
  if k-i in b_after:
    print("Yes")
    exit()
  
print("No")

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cm
"""
