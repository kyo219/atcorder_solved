#!/usr/bin/env python3
# from typing import *

YES = 'Yes'

# def solve(n: int, k: int, a: List[int]) -> str:
def solve(n, k, a):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    n = int(next(tokens))
    k = int(next(tokens))
    a = [None for _ in range(n)]
    for i in range(n):
        a[i] = int(next(tokens))
    assert next(tokens, None) is None
    a1 = solve(n, k, a)
    print(a1)

if __name__ == '__main__':
    main()
