#!/usr/bin/env python3
# from typing import *



# def solve(T: int, P: List[int], Q: List[int], R: List[int]) -> List[str]:
def solve(T, P, Q, R):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    T = int(input())
    P = [None for _ in range(T)]
    Q = [None for _ in range(T)]
    R = [None for _ in range(T)]
    for i in range(T):
        P[i], Q[i], R[i] = map(int, input().split())
    ans = solve(T, P, Q, R)
    for i in range(T):
        print(ans[i])

if __name__ == '__main__':
    main()