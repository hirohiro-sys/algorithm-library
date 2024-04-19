n = int(input())
ans = 0
for i in range(n):
    a = input().split()
    if a[0]=="+": ans += int(a[1])
    if a[0]=="-": ans -= int(a[1])
    if a[0]=="*": ans *= int(a[1])

    if ans<0: 
       ans+=10000
    ans %= 10000
    print(ans)

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ab
"""
