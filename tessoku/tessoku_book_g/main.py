#!/usr/bin/env python3
# from typing import *



# def solve(D: int, N: int, L: List[int], R: List[int]) -> List[str]:
def solve(D, N, L, R):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    D = int(input())
    N = int(input())
    L = [None for _ in range(N)]
    R = [None for _ in range(N)]
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    a = solve(D, N, L, R)
    for i in range(D):
        print(a[i])

if __name__ == '__main__':
    main()
