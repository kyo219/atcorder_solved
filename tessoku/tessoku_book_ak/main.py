#!/usr/bin/env python3
# from typing import *



# def solve(N: int, M: int, B: int, A: List[int], C: List[int]) -> int:
def solve(N, M, B, A, C):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    B = int(next(tokens))
    A = [None for _ in range(N)]
    C = [None for _ in range(M)]
    for i in range(N):
        A[i] = int(next(tokens))
    for i in range(M):
        C[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, M, B, A, C)
    print(a)

if __name__ == '__main__':
    main()