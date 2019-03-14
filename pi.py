#!/usr/bin/python3

from decimal import Decimal, getcontext
import sys

def main():
    k = 100
    if sys.argv:
        k = int(sys.argv[1])
    getcontext().prec = (14*k) + 20
    K, M, L, X, S = 6, Decimal(1), Decimal(13591409), 1, 13591409
    for it in range(1,k+1):
        M = (K**3-(K<<4)) * M / it**3
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
    pi = 426880 * Decimal(10005).sqrt() / S
    pi = str(pi)[:14*k]
    n = 80
    print('\n'.join([pi[i:i+n] for i in range(0, len(pi), n)]))


if __name__ == "__main__":
    main()
