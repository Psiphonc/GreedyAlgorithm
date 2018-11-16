def decompose(n, m):
    if (n < 1 or m < 1):
        return 0
    if n == 1 or m == 1:
        return 1
    if n < m:
        return decompose(n, n)
    if n == m:
        return 1 + decompose(n, m - 1)
    return decompose(n, m - 1) + decompose(n - m, m)


print(decompose(6, 6))
