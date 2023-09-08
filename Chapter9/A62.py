import sys

# 再帰の制限を増やす(スタックオーバーフローを防ぐ)
sys.setrecursionlimit(120000)

# 深さ優先探索のメイン実装
def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)




# 入力
n,m = map(int,input().split())
edges = [list(map(int,input().split())) for _ in range(m)]

# グラフの隣接リストの初期化&構築
G = [list() for _ in range(n+1)]
for a, b in edges:
    G[a].append(b)
    G[b].append(a)

# ノードの訪問状態を管理する配列を初期化
visited = [False] * (n + 1)

# 深さ優先探索
dfs(1, G, visited)

# 答えを一旦Trueで初期化
answer = True

# 判定&出力
for i in range(1,n+1):
    if visited[i] == False:
        answer = False
    
if answer == True:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
