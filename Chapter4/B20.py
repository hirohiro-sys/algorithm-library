# 入力
S = input()
T = input()  

# LCSのための2次元配列を初期化
dp = [[0] * (len(T) + 1) for i in range(len(S) + 1)]

# メイン処理
dp[0][0] = 0
for i in range(len(S) + 1):
    for j in range(len(T) + 1):
        if i >= 1 and j >= 1 and S[i - 1] == T[j - 1]:
            # S[i-1]とT[j-1]が同じ文字ならば編集距離は変化しない
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
        elif i >= 1 and j >= 1:
            # S[i-1]とT[j-1]が異なる場合、1文字置換が必要
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
        elif i >= 1:
            # Tが空文字列の場合、Sの文字列を削除してTと一致させる必要がある
            dp[i][j] = dp[i - 1][j] + 1
        elif j >= 1:
            # Sが空文字列の場合、Tの文字列を挿入してSと一致させる必要がある
            dp[i][j] = dp[i][j - 1] + 1

# 出力
print(dp[len(S)][len(T)])

"""解説はgithubサポートページにある
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cs
"""
