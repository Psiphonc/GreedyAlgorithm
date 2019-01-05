def matrixChain(p, m, s):
    n = len(p) - 1
    for i in range(1, n + 1):
        m[i][i] = 0
    for r in range(2, n + 1):
        for t in range(1, n - r + 2):
            j = t + r - 1
            m[t][j] = m[t + 1][j] + p[t - 1] * p[t] * p[j]
            s[t][j] = t
            for k in range(t + 1, j):
                a = m[t][k] + m[k + 1][j] + p[t - 1] * p[k] * p[j]
                if a < m[t][j]:
                    m[t][j] = a
                    s[t][j] = k


def traceback(s, i, j):
    if i == j:
        return
    traceback(s, i, s[i][j])
    traceback(s, s[i][j] + 1, j)
    print('Multiply A{},{} and A{},{}'.format(i, s[i][j], (s[i][j] + 1), j))


p = [30, 35, 15, 5, 10, 20, 25]
m = [[0 for i in range(7)] for j in range(7)]
s = [[0 for i in range(7)] for j in range(7)]
matrixChain(p, m, s)
# print('m')
# for t in m:
#     print(t)
# print('s')
# for t in s:
#     print(t)
traceback(s, 1, 6)
