#!/usr/bin/env python3
# from typing import *



# def solve(N: int, A: List[int], B: List[int]) -> Tuple[int, List[int]]:
def solve(N, A, B):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N - 1)]
    B = [None for _ in range(N - 2)]
    for i in range(N - 1):
        A[i] = int(next(tokens))
    for i in range(N - 2):
        B[i] = int(next(tokens))
    assert next(tokens, None) is None
    K, P = solve(N, A, B)
    print(K)
    print(*[P[i] for i in range(K)])

if __name__ == '__main__':
    main()
