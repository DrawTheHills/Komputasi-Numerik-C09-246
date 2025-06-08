# f(x) = x^3 + 6x^2 - 19x - 84
# X0 = -4, X1 = 3
# X sebenarnya = -3

# 3 Iterasi Pertama

def fx(x):
    return round(x**3 + 6*x**2 - 19*x - 84, 2)

def secant(xo, x1, xa, n):

    cprev = x1

    for i in range(1, n+1):
        cx = x1 - fx(x1) * (xo - x1) / (fx(xo) - fx(x1))
        cx = round(cx, 2)

        Et = abs((xa - cx) / xa * 100)
        Et = round(Et, 2)

        Ea = abs((cx - cprev) / cx * 100)
        Ea = round(Ea, 2)

        print(f"ITERASI {i}")
        print(f"Xi = {cx:.2f}")
        print(f"Et = {Et:.2f}%")
        print(f"Ea = {Ea:.2f}%\n")

        xo = x1
        x1 = cx
        cprev = cx


secant(-4,3,-3,3)
