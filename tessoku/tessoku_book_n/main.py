#!/usr/bin/env python3
# from typing import *

YES = 'Yes'

# def solve(a: str, b: List[str], c: List[str], d: List[str], e: str) -> str:
def solve(a, b, c, d, e):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    a = next(tokens)
    b = [None for _ in range(a)]
    c = [None for _ in range(a)]
    d = [None for _ in range(a)]
    for i in range(a):
        b[i] = next(tokens)
        c[i] = next(tokens)
        d[i] = next(tokens)
    e = next(tokens)
    assert next(tokens, None) is None
    a1 = solve(a, b, c, d, e)
    print(a1)

if __name__ == '__main__':
    main()
