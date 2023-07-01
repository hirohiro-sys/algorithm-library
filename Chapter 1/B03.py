n = int(input())
li = list(map(int,input().split()))

for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      if li[i]+li[j]+li[k]==1000:
        exit(print("Yes"))
print("No")

'''
# 入力
N = int(input())
A = list(map(int, input().split()))

# 答えを求める
Answer = False
for i in range(N):
	for j in range(i+1, N):
		for k in range(j+1, N):
			if A[i] + A[j] + A[k] == 1000:
				Answer = True

# 出力
if Answer == True:
	print("Yes")
else:
	print("No")
'''
