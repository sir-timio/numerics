def monte_carlo_calc(a, b, f, n):
    K = 0
    fmax = f(b)
    r1 = np.random.uniform(a, b, n)
    r2 = np.random.uniform(0, fmax, n)
    for x, y in zip(r1, r2):
        if f(x) > y:
            K += 1
    return K / n * fmax * (b - a)


def rect_calc(a, b, f, n):
    xs = np.linspace(a, b, n+1)
    h = (b-a)/n
    I = 0
    for x in xs[:-1]:
        I += f(x + h/2)
    I *= h
    return I

def trapezoid_calc(a, b, f, n):
    xs = np.linspace(a, b, n+1)
    h = (b-a)/n
    ys = f(xs)
    I = (f(a) + f(b))/ 2
    I += sum(ys[1:-1])
    I *= h
    return I

def simpson_calc(a, b, f, n):
    assert n % 2 != 1, 'N must be even'
    xs = np.linspace(a, b, n+1)
    h = (b-a)/n
    ys = f(xs)
    I = ys[0] + ys[-1]
    I += 4 * sum([ys[i] for i in range(1, n, 2)])
    I += 2 * sum([ys[i] for i in range(2, n-1, 2)])
    I *= h/3
    return I