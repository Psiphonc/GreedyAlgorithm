def calcWeight(i, j, k):
    return weight[i][j] + weight[j][k] + weight[k][i]


def traceback(s, i, j):
    if i == j:
        return
    traceback(s, i, int(s[i][j]))
    traceback(s, int(s[i][j] + 1), j)
    print('v' + str(i - 1) + ',v' + str(s[i][j]) + ',v' + str(j))


global weight
weight = [[0, 2, 2, 3, 1, 4],
          [2, 0, 1, 5, 2, 3],
          [2, 1, 0, 2, 1, 4],
          [3, 5, 2, 0, 6, 2],
          [1, 2, 1, 6, 0, 1],
          [4, 3, 4, 2, 1, 0]]
n = 6
t = [[0 for x in range(n)] for y in range(n)]
s = [[0 for x in range(n)] for y in range(n)]
for i in range(1, n):
    t[i][i] = 0
for r in range(2, n):
    for i in range(1, n - r + 1):
        j = i + r - 1
        t[i][j] = t[i + 1][j] + calcWeight(i - 1, i, j)
        s[i][j] = i
        for k in range(i + 1, j):
            u = t[i][k] + t[k + 1][j] + calcWeight(i - 1, k, j)
            if u < t[i][j]:
                t[i][j] = u
                s[i][j] = k

traceback(s, 1, 5)
