import math
a,b = map(int,input().split())
print(math.gcd(a,b))


"""ユークリッド互除法
def GCD(A, B):
	while A >= 1 and B >= 1:
		if A >= B:
			A = A % B 
		else:
			B = B % A 
	if A >= 1:
		return A
	return B

A, B = map(int, input().split())
print(GCD(A, B))
"""

"""
https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_o
"""
