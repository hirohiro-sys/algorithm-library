# 入力
T = int(input())
N = int(input())
L = [ None ] * N
R = [ None ] * N
for i in range(N):
    L[i],R[i] = map(int,input().split())

#前の時刻との差
B = [ 0 ] * (T + 1)
for i in range(N):
    B[L[i]] += 1
    B[R[i]] -= 1

#累積和
Answer = [ None ] * (T + 1)
Answer[0] = B[0]
for i in range(1,T+1):
    Answer[i] = Answer[i-1] + B[i]

#出力
for i in range(T):
    print(Answer[i])

'''
これもいもす法
'''
