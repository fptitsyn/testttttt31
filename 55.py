from itertools import *


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


m, mx = 0, 0
for x in range(100, 1001):
    s = str(x)
    a = ["".join(c) for c in set(permutations(s, r=2))]
    a = [x for x in a if x[0] != "0" and is_prime(int(x))]
    if mx <= len(a):
        mx = len(a)
        m = x

print(m)
