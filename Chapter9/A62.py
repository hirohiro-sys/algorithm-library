# これないとエラーなる
import sys
sys.setrecursionlimit(10 ** 6)

n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

visited = [False] * n
def dfs(v):
    if visited[v]:
        return
    visited[v] = True
    for i in g[v]:
        if not visited[i]:
            dfs(i)
        
dfs(0)
if all(visited):
    print("The graph is connected.")
else:
    print("The graph is not connected.")

"""
https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_am
"""
