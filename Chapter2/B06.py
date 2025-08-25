N = int(input())
A = list(map(int,input().split()))

atari = [0] * (N+1)
hazure = [0] * (N+1)
for i in range(1,N+1):
  # 直前の値から+1をするため
  atari[i] = atari[i-1]
  if A[i-1]==1:
    atari[i] += 1
  # 直前の値から+1をするため
  hazure[i] = hazure[i-1]
  if A[i-1]==0:
    hazure[i] += 1
    
Q = int(input())
for _ in range(Q):
  L,R = map(int,input().split())
  atari_cnt = atari[R]-atari[L-1]
  hazure_cnt = hazure[R]-hazure[L-1]
  if atari_cnt > hazure_cnt:
    print("win")
  elif atari_cnt < hazure_cnt:
    print("lose")
  else:
    print("draw")

"""問題URL
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ce
"""
