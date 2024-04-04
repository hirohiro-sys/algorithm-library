n = int(input())
a = list(map(int,input().split()))
atari = [0] * (n+1)
hazre = [0] * (n+1)
for i in range(1,n+1):
  atari[i] = atari[i-1]
  if a[i-1]==1:
    atari[i] += 1
  hazre[i] = hazre[i-1]
  if a[i-1]==0:
    hazre[i] += 1
q = int(input())
for i in range(q):
  a,b = map(int,input().split())
  count_atari = atari[b]-atari[a-1]
  count_hazre = hazre[b]-hazre[a-1]
  if count_atari>count_hazre:
    print("win")
  elif count_atari<count_hazre:
    print("lose")
  else:
    print("draw")

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ce
"""
