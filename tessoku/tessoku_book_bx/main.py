#!/usr/bin/env python3
# from typing import *

MOD = 1000000007

# def solve(N: int, W: int, L: int, R: int, X: List[int]) -> int:
def solve(N, W, L, R, X):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    W = int(next(tokens))
    L = int(next(tokens))
    R = int(next(tokens))
    X = [None for _ in range(N)]
    for i in range(N):
        X[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, W, L, R, X)
    print(a)

if __name__ == '__main__':
    main()
