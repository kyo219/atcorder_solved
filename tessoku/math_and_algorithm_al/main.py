#!/usr/bin/env python3
# from typing import *



# def solve(T: int, N: int, L: List[int], R: List[int]) -> List[str]:
def solve(T, N, L, R):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    T = int(input())
    N = int(input())
    L = [None for _ in range(N)]
    R = [None for _ in range(N)]
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    ans = solve(T, N, L, R)
    for i in range(T):
        print(ans[i])

if __name__ == '__main__':
    main()
