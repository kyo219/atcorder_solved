#!/usr/bin/env python3
# from typing import *



# def solve(Q: str, Query: List[str]) -> Tuple[int, int]:
def solve(Q, Query):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    Q = input()
    Query = [None for _ in range(Q)]
    for i in range(Q):
        Query[i] = input()
    a, b = solve(Q, Query)
    print(a)
    print(b)

if __name__ == '__main__':
    main()
