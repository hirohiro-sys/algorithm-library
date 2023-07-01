a,b = map(int,input().split())
li = [1,2,4,5,10,20,25,50,100]
for i in range(a,b+1):
  if i in li:
    exit(print("Yes"))
print("No")

'''
# 入力
A, B = map(int, input().split())

# 答えを求める
Answer = False
for i in range(A, B + 1):
	if 100 % i == 0:
		Answer = True

# 出力
if Answer == True:
	print("Yes")
else:
	print("No")
'''
