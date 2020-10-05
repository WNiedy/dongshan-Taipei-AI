a = []
b = []

a.append(0)
b.append(0)

for i in range(1, 101):
    b.append(i)

for j in range(1, 100):
    a.append(b[j] + a[j-1])

print(a[50]-a[30])