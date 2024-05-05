n=int(input())

l,r=0,10**9
while l+0.001<r:
    x=(l+r)/2
    if x**3+x>=n:
        r=x
    else:
        l=x
print(l)

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ck
"""
