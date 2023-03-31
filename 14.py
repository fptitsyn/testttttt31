def f(x, q):
    a = 0
    x = x[::-1]
    for i in range(len(x)):
        a += x[i] * q ** i
    return a


def f1(x, q):
    a = []
    while x > 0:
        a.append(x % q)
        x //= q
    return list(reversed(a))


for x in range(10):
    a1 = f([3, x, 1, 5, x], 15)
    a2 = f([1, 2, 3], int(f"3{x}51"))
    a3 = x ** x
    a4 = f([1, x, 3], int(f"1{x}3"))
    a5 = f([1, x, 2], x + 1)
    d = a1 + a2 + a3 + a4 + a5
    if d % 13 == 0:
        print(x, f1(d // 13, 13))
