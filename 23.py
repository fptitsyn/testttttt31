def f(x, y, s):
    if x == y and s.count("3") == 1:
        return 1
    if x > y:
        return 0
    return f(x + 1, y, s + "1") + f(x + 2, y, s + "2") + f(x * 2, y, s + "3")


print(f(2, 12, ""))
