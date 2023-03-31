def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


mx = 0
for i in range(100, 1000):
    s = str(i)
    c = 0
    a = [s[0] + s[1], s[0] + s[2], s[1] + s[0], s[2] + s[0], s[1] + s[2], s[2] + s[1]]
    for j in a:
        if is_prime(int(j)):
            c += 1
    mx = max(mx, c)
    if c == mx:
        print(i)

