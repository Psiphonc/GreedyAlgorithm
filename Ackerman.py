def Ackerman(n, m):
    if n == 1 and m == 0:
        return 2
    elif n == 0 and m >= 0:
        return 1
    elif n >= 2 and m == 0:
        return n + 2
    else:
        return Ackerman(Ackerman(n - 1, m), m - 1)


print(Ackerman(2, 2))
