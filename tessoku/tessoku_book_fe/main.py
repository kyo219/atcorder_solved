#!/usr/bin/env python3
# from typing import *



# def solve(N: int, C: List[int], Q: int, X: List[int]) -> List[str]:
def solve(N, C, Q, X):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    C = [None for _ in range(N)]
    for i in range(N):
        C[i] = int(next(tokens))
    Q = int(next(tokens))
    X = [None for _ in range(Q)]
    for i in range(Q):
        X[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, C, Q, X)
    for i in range(Q):
        print(a[i])

if __name__ == '__main__':
    main()