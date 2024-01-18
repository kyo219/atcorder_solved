#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    H = random.randint(1, 10)  # TODO: edit here
    W = random.randint(1, 10)  # TODO: edit here
    c = [[None for _ in range(H + W + 4)] for _ in range(H + W + 4)]
    for j in range(H + 4):
        for i in range(W):
            c[i + j][i + j] = random.randint(1, 10)  # TODO: edit here
    print(H, W)
    for j in range(H + 4):
        print(*[c[i + j][i + j] for i in range(W)])

if __name__ == "__main__":
    main()
