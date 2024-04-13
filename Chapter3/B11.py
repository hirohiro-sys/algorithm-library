import bisect
n,a = int(input()),sorted(map(int,input().split()))
for i in range(int(input())): print(bisect.bisect_left(a,int(input())))

"""
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cj
"""
