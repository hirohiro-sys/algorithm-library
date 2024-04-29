import sys
sys.setrecursionlimit(1 << 20)

n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

# ここの処理の流れがわかりづらかったら公式のGithub見るといい
visited = [False] * n
path = []
def dfs(v):
    path.append(v)
    if v==n-1:
        for i in path:
            print(i+1)
        exit()
    visited[v]=True
    for j in g[v]:
        if not visited[j]:
            dfs(j)
    path.pop()

dfs(0)

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ei
"""
