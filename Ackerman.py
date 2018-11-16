def ackerman(n, m):
    if n == 1 and m == 0:
        return 2
    elif n == 0 and m >= 0:
        return 1
    elif n >= 2 and m == 0:
        return n + 2
    else:
        return ackerman(ackerman(n - 1, m), m - 1)


n = int(input("n:"))
m = int(input("m:"))
print(ackerman(n, m))
