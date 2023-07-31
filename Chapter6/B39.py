import heapq


G = [list() for _ in range(2005)] # G[i] は i 日目から始まる仕事の給料のリスト

# 入力
N, D = map(int, input().split())
for _ in range(N):
	X, Y = map(int, input().split())
	G[X].append(Y)

# 答えを求める
Q = []
Answer = 0
for i in range(1, D + 1):
	# i 日目から始まる仕事をキューに追加
	# heap は最小値を取り出すので -1 倍する
	for y in G[i]: heapq.heappush(Q, -y)

	# やる仕事を選択し、その仕事をキューから削除する
	if Q:
		Answer -= heapq.heappop(Q)

# 出力
print(Answer)


"""(TLEする解答)
# 入力
N, D = map(int, input().split())
X = [ None ] * N
Y = [ None ] * N
for i in range(N):
	X[i], Y[i] = map(int, input().split())

# 配列の準備
# used[i] は仕事 i を選んだかどうか
used = [ False ] * N

# 答えを求める
Answer = 0
for i in range(1, D+1):
	maxValue = 0 # 給料の最大値
	maxID = -1   # 給料が最大となる仕事の番号
	for j in range(N):
		if used[j] == False and maxValue < Y[j] and X[j] <= i:
			maxValue = Y[j]
			maxID = j

	# 選べる仕事がある場合
	if maxID != -1:
		Answer += maxValue
		used[maxID] = True

# 出力
print(Answer)
"""
