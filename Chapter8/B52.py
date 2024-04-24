from collections import deque

n,x = map(int,input().split())
s = list(input())
x -= 1

queue = deque([x])
s[x] = "@"
while queue:
    pos = queue.popleft()
    # インデックスは0~n-1のため以下の条件文になる
    if 0<=pos-1 and s[pos-1]==".":
        s[pos-1]="@"
        queue.append(pos-1)
    if pos+1<n and s[pos+1]==".":
        s[pos+1]="@"
        queue.append(pos+1)

print("".join(s))

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dy
"""
