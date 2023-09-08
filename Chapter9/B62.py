import sys

sys.setrecursionlimit(1 << 20)

# 入力
n, m = map(int,input().split())

# 隣接リスト初期化&構築
g  = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    g[a-1].append(b)
    g[b-1].append(a)

# ノードの訪問状態管理配列を初期化
visited = [False] * n

# パスを記録するリスト
path = []

# 深さ優先探索メイン実装
def dfs(i: int):
    path.append(i)

    if i==n - 1:
        for x in path:
            print(x + 1)
        exit(0)

    visited[i] = True
    for j in g[i]:
        if not visited[j]:
            dfs(j)
    path.pop()

# 深さ優先探索
dfs(0)
