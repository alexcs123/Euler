from math import prod, sqrt, comb, factorial
from string import ascii_uppercase
from sympy import n_order, multiplicity
from data import *


def p001():
    return sum([n for n in range(1000) if not n % 3 or not n % 5])


def p002():
    f = [1, 2]
    while f[-1] <= 4000000:
        f.append(f[-1] + f[-2])
    return sum([n for n in f if not n % 2])


def p003():
    d, n = 1, 600851475143
    while n >= d ** 2:
        d += 1
        while not n % d:
            n /= d
    return d if n == 1 else int(n)


def p004():
    return max([a * b for a in range(1000) for b in range(a + 1) if str(a * b) == str(a * b)[::-1]])


def p005():
    m = 2
    for f in range(3, 21):
        a, b, c = m, f, f
        while a % b:
            c = a % b
            a, b = b, c
        m = (m * f) / c
    return int(m)


def p006():
    return sum(range(101)) ** 2 - sum([n ** 2 for n in range(101)])


def p007():
    l, c = [2], 1
    while len(l) < 10001:
        c, p = c + 2, True
        for d in l:
            if not c % d:
                p = False
                break
        if p:
            l.append(c)
    return l[-1]


def p008():
    p, n = 0, d008
    for i in range(len(n) - 12):
        p = max(p, prod([int(d) for d in n[i:i + 13]]))
    return p


def p009():
    for a in range(333):
        for b in range(a + 1, 500):
            if a ** 2 + b ** 2 == (1000 - a - b) ** 2:
                return a * b * (1000 - a - b)


def p010():
    s, c = 2, 1
    while c < 1999998:
        c, p = c + 2, True
        for d in range(3, int(sqrt(c)) + 1, 2):
            if not c % d:
                p = False
                break
        if p:
            s += c
    return s


def p011():
    p, g = 0, d011
    for y in range(len(g)):
        for x in range(len(g) - 3):
            p = max(p, g[y][x] * g[y][x + 1] * g[y][x + 2] * g[y][x + 3], g[x][y] * g[x + 1][y] * g[x + 2][y] * g[x + 3][y])
    for y in range(len(g) - 3):
        for x in range(len(g) - 3):
            p = max(p, g[y][x] * g[y + 1][x + 1] * g[y + 2][x + 2] * g[y + 3][x + 3], g[y + 3][x] * g[y + 2][x + 1] * g[y + 1][x + 2] * g[y][x + 3])
    return p


def p012():
    t, n, d = 0, 1, 0
    while d <= 500:
        t, n, d = t + n, n + 1, 1 if sqrt(t + n).is_integer() else 0
        for c in range(1, int(sqrt(t))):
            d += 2 if not t % c else 0
    return t


def p013():
    return int(str(sum(d013))[:10])


def p014():
    m, d = 0, 0
    for n in range(2, 1000000):
        c, x = 0, n
        while n > 1:
            c += 1
            n = n / 2 if not n % 2 else 3 * n + 1
        if c > m:
            m, d = c, x
    return d


def p015():
    return comb(40, 20)


def p016():
    return sum([int(d) for d in str(2 ** 1000)])


def p017():
    s, d = 0, {
        '00': '',
        '01': 'one',
        '02': 'two',
        '03': 'three',
        '04': 'four',
        '05': 'five',
        '06': 'six',
        '07': 'seven',
        '08': 'eight',
        '09': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '20': 'twenty',
        '30': 'thirty',
        '40': 'forty',
        '50': 'fifty',
        '60': 'sixty',
        '70': 'seventy',
        '80': 'eighty',
        '90': 'ninety'
    }
    for n in range(1001):
        a = str(n).zfill(4)
        s += len(d['0' + a[0]]) + len(d['0' + a[1]])
        s += len('thousand') if a[0] != '0' else 0
        s += len('hundred') if a[1] != '0' else 0
        s += len('and') if a[2:] != '00' and a[:2] != '00' else 0
        s += len(d[a[2:]]) if int(a[2:]) <= 20 or a[3] == '0' else len(d[a[2] + '0']) + len(d['0' + a[3]])
    return s


def p018():
    m, t = 0, d018
    for c in range(2 ** (len(t) - 1)):
        b = [int(d) for d in str(bin(c))[2:].zfill(len(t))]
        s = sum([t[r][c] for r, c in enumerate([sum(b[:i + 1]) for i in range(len(b))])])
        m = s if s > m else m
    return m


def p019():
    s, d, n, m, y = 0, 1, 1, 1, 1900
    while y < 2001:
        s += 1 if (d, n) == (7, 1) and y > 1900 else 0
        d, n = d % 7 + 1, n + 1
        n, m = (1, m % 12 + 1) if n == 32 or n == 31 and m in [4, 6, 9, 11] or (n, m) == (30, 2) or (n, m) == (29, 2) and (y % 4 or not y % 100) and y % 400 else (n, m)
        y += 1 if (n, m) == (1, 1) else 0
    return s


def p020():
    return sum([int(d) for d in str(prod(range(2, 101)))])


def p021():
    p = []
    for a in range(10000):
        b, s = 1, 1
        for d in range(2, a // 2 + 1):
            b += d if not a % d else 0
        for d in range(2, b // 2 + 1):
            s += d if not b % d else 0
        p.append([a, b]) if a == s else None
    return sum([a[0] for a in p if a[0] != a[1]])


def p022():
    return sum([(v + 1) * sum([{l: v + 1 for v, l in enumerate(ascii_uppercase)}[x] for x in n]) for v, n in enumerate(sorted(open('p022_names.txt').read().replace('\"', '').split(',')))])


def p023():
    a = [n for n in range(12, 28123) if sum([f for f in range(1, n // 2 + 1) if not n % f]) > n]
    s = list(set([a[i] + a[j] for i in range(len(a)) for j in range(i + 1)]))
    return sum([x for x in range(28123) if x not in s])


def p024():
    d, p, n = list(range(10)), 999999, ''
    while len(d):
        n, p = n + str(d.pop(p // factorial(len(d) - 1))), p % factorial(len(d))
    return int(n)


def p025():
    f = [1, 1]
    while len(str(f[-1])) < 1000:
        f.append(f[-1] + f[-2])
    return len(f)


def p026():
    d, m = 0, 0
    for c in range(2, 1000):
        n = n_order(10, c // 2 ** multiplicity(2, c) // 5 ** multiplicity(5, c))
        d, m = (c, n) if n > m else (d, m)
    return d


def p027():
    m, ma, mb = 0, 0, 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while True:
                c = abs(n ** 2 + a * n + b)
                p = True if c % 2 else False
                if p:
                    for d in range(3, int(sqrt(c)) + 1, 2):
                        if not c % d:
                            p = False
                            break
                if not p:
                    m, ma, mb = (n, a, b) if n > m else (m, ma, mb)
                    break
                n += 1
    return ma * mb


def p028():
    return sum([16 * n ** 2 + 4 * n + 4 for n in range(501)]) - 3


def p029():
    l = []
    for a in range(2, 101):
        for b in range(2, 101):
            l.append(a ** b) if a ** b not in l else None
    return len(l)


def p030():
    s, n = 0, 10
    while n <= 9 ** 5 * 5:
        s, n = s + n if sum([int(d) ** 5 for d in str(n)]) == n else s, n + 1
    return s


def p031():
    def r(p, c):
        if not p or c == [1]:
            nonlocal n
            n += 1
        else:
            for i in range(p // max(c) + 1):
                r(p - i * max(c), c[:-1])
    n = 0
    r(200, [1, 2, 5, 10, 20, 50, 100, 200])
    return n


def p034():
    s, n = 0, 10
    while n <= 40585:
        s, n = s + n if n == sum([factorial(int(i)) for i in str(n)]) else s, n + 1
    return s


def p035():
    d, p = 2, [False, False] + [True for _ in range(999998)]
    while d ** 2 < len(p):
        if p[d]:
            for n in range(d ** 2, len(p), d):
                p[n] = False
        d += 1
    p = ['2', '5'] + [str(n) for n in range(len(p)) if p[n] and all(d not in str(n) for d in ['0', '2', '4', '5', '6', '8'])]
    return len([n for n in p if all(c in p for c in [n[d:] + n[:d] for d in range(len(n))])])


def p036():
    return sum([n for n in range(1, 1000000) if str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[:1:-1]])


def p039():
    l, m = 0, 0
    for p in range(12, 1001):
        n = 0
        for a in range(1, 1 + int(p // 3.41421)):
            n += 1 if (p / 2 * (p - 2 * a) / (p - a)).is_integer() else 0
        l, m = (p, n) if n > m else (l, m)
    return l


def p040():
    return prod([int(''.join(str(n) for n in range(22223))[10 ** e]) for e in range(6)])


def p042():
    return len([s for s in open('p042_words.txt').read().replace('\"', '').split(',') if sum([{ascii_uppercase[i]: i + 1 for i in range(26)}[l] for l in s]) in [int((i ** 2 + i) / 2) for i in range(1, 21)]])


def p048():
    return int(str(sum([n ** n for n in range(1, 1001)]))[-10:])


def p053():
    c = 0
    for n in range(101):
        for r in range(n):
            c += 1 if comb(n, r) > 1000000 else 0
    return c


def p056():
    m = 0
    for a in range(100):
        for b in range(100):
            m = max(m, sum([int(n) for n in str(a ** b)]))
    return m


def p067():
    t = [[int(n) for n in r.split(' ')] for r in open('p067_triangle.txt').read().split('\n')[:-1]]
    for r in range(len(t) - 2, -1, -1):
        for n in range(len(t[r])):
            t[r][n] += max(t[r + 1][n], t[r + 1][n + 1])
    return t[0][0]


def p097():
    return int(str(28433 * 2 ** 7830457 + 1)[-10:])


def p206():
    for n in range(1010101010, 1389026630, 10):
        if str(n ** 2)[::2] == '1234567890':
            return n
