def lcs(i, j, x, b):
    if i == 0 or j == 0:
        return
    if b[i][j] == 1:
        lcs(i - 1, j - 1, x, b)
        print(x[i])
    elif b[i][j] == 2:
        lcs(i - 1, j, x, b)
    else:
        lcs(i, j - 1, x, b)


x = [' ', 'A', 'B', 'C', 'B', 'D', 'A', 'B']
y = [' ', 'B', 'D', 'C', 'A', 'B', 'A']
m = len(x) - 1
n = len(y) - 1
c = [[0 for x in range(n + 2)] for y in range(m + 2)]
b = [[0 for x in range(n + 2)] for y in range(m + 2)]
for i in range(1, m + 1):
    c[i][0] = 0
for i in range(1, n + 1):
    c[0][i] = 0
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if x[i] == y[j]:
            c[i][j] = c[i - 1][j - 1] + 1
            b[i][j] = 1
        elif c[i - 1][j] >= c[i][j - 1]:
            c[i][j] = c[i - 1][j]
            b[i][j] = 2
        else:
            c[i][j] = c[i][j - 1]
            b[i][j] = 3
print(c[m][n])
print()
lcs(m, n, x, b)
