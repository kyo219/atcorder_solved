#!/usr/bin/env python3
# from typing import *



# def solve(N: int, A: List[int], D: int, L: List[int], R: List[int]) -> Tuple[int, int]:
def solve(N, A, D, L, R):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    D = int(next(tokens))
    L = [None for _ in range(D)]
    R = [None for _ in range(D)]
    for i in range(D):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    assert next(tokens, None) is None
    c, d = solve(N, A, D, L, R)
    print(c)
    print(d)

if __name__ == '__main__':
    main()
