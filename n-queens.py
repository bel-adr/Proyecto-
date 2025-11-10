"""
Discrete Mathematics and Its Applications
---------------------------------------------------
Members: Isabel Adrada, Juan Guevara, Maria Gil, Juan de la Peña
Class: A
"""
from math import log10, floor, comb

#verificación si dos reinas están en la misma fila
def row(x1, x2):
    return x1 != x2

# verificación si dos reinas están en la misma columna
def col(y1, y2):
    return y1 != y2

# verificación si dos reinas están en la misma diagonal
def diag(x1, y1, x2, y2):
    return (y2 - y1 != x2 - x1) and (y2 - y1 != -x2 + x1);

# determinación de la validez de una combinación de reinas
def nqueens(l, n):
    ans = True
    i = 0
    while i < len(l) and ans:
        j = i + 1
        while j < len(l) and ans:
            ans = row(l[i][0], l[j][0]) and col(l[i][1], l[j][1]) and diag(l[i][0], l[i][1], l[j][0], l[j][1])
            j += 1
        i += 1
    return ans

# cálculo de la cantidad de combinaciones para un tablero de dimensión n
def configurations(n):
    return comb(n*n, n)

# formato en notación científica
def sn_format(n):
    signo = "-" if n < 0 else ""
    n_abs = abs(n)
    e = floor(log10(n_abs))
    mantisa_int = round(n_abs / 10**(e - 4))
    mantisa_str = str(mantisa_int)
    if len(mantisa_str) > 5:
        mantisa_str = mantisa_str[:5]
        e += 1
    return f"{signo}{mantisa_str[0]}.{mantisa_str[1:]} x 10^{e}"

# lectura de datos y output
def main():
    m = int(input())
    for i in range(m):
        n = int(input())
        l = []
        for j in range(n):
            x, y = input().split(", ")
            x = int(x)
            y = int(y)
            l.append([x, y])
        a, b = input().split(", ")
        pos = "Yes" if nqueens(l, n) else "No"
        config = configurations(n)
        num = str(config) if config <= 10000000000 else sn_format(config)
        print("Case ", i + 1, ":", sep="")
        print("Satisfies ", n, "-queen(s) problem? -> ", pos, sep="")
        print("Total Possible Configurations for ", n, "-queen(s): ", num, " configurations", sep="")
        print()
    return 0

main()
