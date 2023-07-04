#入力
D = int(input())
N = int(input())
L = [ None ] * N
R = [ None ] * N
for i in range(N):
    L[i],R[i] = map(int,input().split())
#前日比
B = [ 0 ] * (D+2)
for i in range(N):
    B[L[i]] += 1
    B[R[i]+1] -= 1
#累積和
Answer = [ None ] * (D+2)
Answer[0] = 0
for i in range(1,D+1):
    Answer[i] = Answer[i - 1] + B[i]

#出力
for i in range(1,D+1):
    print(Answer[i])

'''
差分(前日比など)を計算した後に累積和をとるテクニックをいもす法という
'''
