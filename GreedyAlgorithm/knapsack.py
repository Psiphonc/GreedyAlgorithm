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
    elements = []
    for i in range(0, n):
        elements.append(Element(w[i], v[i], i))
    sorted(elements)
    opt = 0.0
    i = 0
    for i, e in enumerate(elements):
        x[i] = 0
        if e.weight < c:
            x[e.index] = 1
            opt += e.value
            c -= e.weight
        else:
            break
    if c > 0:
        d = elements[i]
        x[d.index] = c / d.weight
        opt += x[d.index] * d.value
    return opt


def knapsac01(c, w, v, x):
    opt = 0.0
    elements = []
    for i, ww in enumerate(w):
        elements.append(Element(ww, v[i], i))
    sorted(elements)
    for e in elements:
        if e.weight < c:
            c -= e.weight
            opt += e.value
            x[e.index] = 1
    return opt


c = 50
w = [10, 20, 30]
v = [60, 100, 120]
x = [0] * 3

print('背包问题：'+str(knapsac(c, w, v, x)) + '  ' + x.__str__())
x = [0] * 3
print('01背包问题:'+str(knapsac01(c, w, v, x)) + '  ' + x.__str__())
