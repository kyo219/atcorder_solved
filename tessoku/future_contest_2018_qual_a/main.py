#!/usr/bin/env python3
# from typing import *



# def solve(A: List[List[str]]) -> Tuple[str, List[str], List[str], List[str]]:
def solve(A):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    A = [[None for _ in range(2 * N + 2)] for _ in range(2 * N + 2)]
    import sys
    tokens = iter(sys.stdin.read().split())
    for j in range(N + 2):
        for i in range(N):
            A[i + j][i + j] = next(tokens)
    assert next(tokens, None) is None
    Q, X, Y, H = solve(A)
    print(Q)
    for i in range(Q):
        print(X[i], Y[i], H[i])

if __name__ == '__main__':
    main()
