n,k = map(int,input().split())
count = 0
for i in range(1,n+1):
  for j in range(1,n+1):
    tmp = k - i - j
    if 1<=tmp<=n:
      count+=1
print(count)

'''
# 入力
N, K = map(int, input().split())
Answer = 0

# 全探索
for x in range(1, N+1):
	for y in range(1, N+1):
		z = K - x - y
		if z >= 1 and z <= N:
			Answer += 1

# 出力
print(Answer)
'''
