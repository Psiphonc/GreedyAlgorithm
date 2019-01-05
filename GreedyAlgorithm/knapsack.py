from functools import total_ordering


@total_ordering
class Element:
    weight = 0
    value = 0
    index = 0
    vpw = 0.0

    def __init__(self, w, v, i):
        self.weight = w
        self.value = v
        self.index = i
        self.vpw = v / w

    def __le__(self, other):
        return self.vpw - other.vpw < 0

    def __eq__(self, other):
        return self.vpw - other.vpw == 0


def knapsac(c, w, v, x):
    n = len(v)
    d = []
    for i in range(0, n):
        d.append(Element(w[i], v[i], i))
    sorted(d)
    opt = 0.0
    for i in x:
        i = 0
    flag = 0
    for i in d:
        if i.weight > c:
            flag = i.index
            break
        x[i.index] = 1
        opt += i.value
        c -= i.weight
    if flag != 0:
        x[d[flag].index] = c / d[flag].weight
        opt += x[d[flag].index] * d[flag].value
    return opt


c = 50
w = [10, 20, 30]
v = [60, 100, 120]
x = [0] * 3

print(knapsac(c, w, v, x))
