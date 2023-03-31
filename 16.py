from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(100000)


@lru_cache(None)
def f(n):
    if n <= 15:
        return n * n + 11
    if n % 2 == 0:
        return f(n // 2) + n * n * n - 5 * n
    return f(n - 1) + 2 * n + 3


c = 0
for i in range(1, 1001):
    k = f(i)
    if str(k).count("6") >= 3:
        c += 1

print(c)
