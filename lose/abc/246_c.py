"""問題文
以下を満たす, X_i (1~N) が存在するか？
X_i = A_i | B_i
abs(X_i - X_{i+1}) <= K

idea
ダメなケースが１度でもあるか否かで判定する.

memo:
これではだめで、やはりDP等で、探索の幅を狭めながらちゃんと見るべきらしい・・・
勉強してから戻ってくる・・
"""


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


# 例:
N=5
K=4
A=[9,8,3,7,2]
B=[1,6,2,9,5]

N = 4
K = 1000000000
A = [1, 1, 1000000000, 1000000000]
B = [1, 1000000000, 1, 1000000000]


# 処理
def is_exit(N, K, A, B):
    score = 0
    for i in range(N-1):
        if abs(A[i] - A[i+1]) > K:
            pass
        elif abs(A[i] - B[i+1]) >K:
            pass
        elif abs(B[i] - A[i+1]) >K:
            pass
        elif abs(B[i] - B[i+1]) >K:
            pass
        else:
            score+=1
    if score==N-1:
        print("Yes")
    else:
        print('No')

is_exit(N, K, A, B)

