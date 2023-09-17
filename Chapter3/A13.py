# 入力
N,K = map(int,input().split())
A = list(map(int,input().split()))

R = [ None ] * N

# しゃくとり法
for i in range(N-1):
  # スタート地点
  if i==0:
    R[i] = 0
  else:
    R[i] = R[i - 1]
  # 限界まで増やす(この部分は図で見るとわかりやすい)
  while R[i] < N-1 and A[R[i]+1]-A[i] <= K:
    R[i] += 1

# 出力
Answer = 0
for i in range(N-1):
  Answer += (R[i] - i)
print(Answer)
