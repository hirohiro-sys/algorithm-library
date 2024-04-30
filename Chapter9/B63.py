# 入力
H,W = map(int,input().split())
sx,sy = map(int,input().split())
sx -= 1
sy -= 1
gx,gy = map(int,input().split())
gx -= 1
gy -= 1
S = [input() for _ in range(H)]

# 無限大の定義とコストの初期化
INF = 1<<61
cost = [[INF]*W for _ in range(H)]

# マスを移動する処理
q = []
def push(x,y,c):
    # 壁がある場合
    if S[x][y] == "#":
        return
    # 現在のコストが既存のコストより低い場合
    if cost[x][y]<=c:
        return
    cost[x][y] = c
    q.append((x,y))

# スタート地点を追加してBFS実行
push(sx,sy,0)
for x,y in q:
    c2 = cost[x][y] + 1
    push(x - 1, y, c2)
    push(x, y - 1, c2)
    push(x + 1, y, c2)
    push(x, y + 1, c2)

# ゴール地点のコストを出力
print(cost[gx][gy])
