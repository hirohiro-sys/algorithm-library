# H, Wの入力を受け取り、行列のサイズを設定
H, W = map(int, input().split())

# スタート地点の座標を受け取り、0-indexedに変換
sx, sy = map(int, input().split())
sx -= 1
sy -= 1

# ゴール地点の座標を受け取り、0-indexedに変換
gx, gy = map(int, input().split())
gx -= 1
gy -= 1

# 迷路の情報を行ごとに受け取り、2次元リストSに格納
S = [input() for _ in range(H)]

# 無限大を表す値を設定
INF = 1 << 61

# 各セルの最短コストを格納する2次元リストcostを無限大で初期化
cost = [[INF] * W for _ in range(H)]

# 幅優先探索用のキューqを初期化
q = []

# 幅優先探索を行う関数pushを定義
def push(x: int, y: int, c: int):
    # ゴール地点または壁の場合は何もせずに終了
    if S[x][y] == '#' or cost[x][y] <= c:
        return
    # 最短コストを更新し、キューに座標を追加
    cost[x][y] = c
    q.append((x, y))

# スタート地点の最短コストを0に設定し、キューに追加
push(sx, sy, 0)

# 幅優先探索を行う
for x, y in q:
    c2 = cost[x][y] + 1
    # 上下左右のセルに対してpush関数を呼び出し、最短コストを更新
    push(x - 1, y, c2)
    push(x, y - 1, c2)
    push(x + 1, y, c2)
    push(x, y + 1, c2)

# ゴール地点の最短コストを出力
print(cost[gx][gy])
