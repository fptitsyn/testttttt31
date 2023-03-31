f = open("17.txt")
a = [int(i) for i in f]
s = ""

for i in a:
    if i > 0:
        s += str(i)[0]
    else:
        s += str(i)[1]
print(s)
ss = sum([int(i) for i in s])

ans = []
for i in range(len(a) - 1):
    if a[i] * a[i + 1] > ss:
        ans.append(a[i] + a[i + 1])

print(len(ans), max(ans))
