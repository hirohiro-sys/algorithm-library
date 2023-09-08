from collections import deque

# 入力
n,m = map(int,input().split())

edges = [list(map(int,input().split())) for _ in range(m)]

# 隣接リストの初期化と構築
G = [[] for i in range(n+1)]
for a,b in edges:
    G[a].append(b)
    G[b].append(a)

# 各頂点までの距離を保持するリストdistを初期化
dist = [-1] * (n + 1)

# 始点からの距離を初期化
dist[1] = 0

# 幅優先探索のキューを初期化
Q = deque()
Q.append(1)

# 幅優先探索メイン処理
while len(Q) >= 1:
    pos = Q.popleft()
    for nex in G[pos]:
        if dist[nex] == -1:
            dist[nex] = dist[pos] + 1
            Q.append(nex)

for i in range(1,n + 1):
    print(dist[i])


'''
書籍の図を見ながらコードを見ていくとわかりやすい
'''
