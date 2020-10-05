def f(x):
    if x == 0:
        return 0                                             
    elif x == 1:
        return 1
    else:
        return f(x-1)+f(x-2)

for i in range(0, 10):
    print(f(i))

print("")

print(f(12))