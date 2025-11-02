"""
Discrete Mathematics and Its Applications
---------------------------------------------------
Members: Isabel Adrada, Juan Guevara, Maria Gil, Juan de la Peña
Class: A
"""
from math import log10, floor, comb

def hor(x1, x2):
    return x1 == x2

def ver(y1, y2):
    return y1 == y2

def diag(x1, y1, x2, y2):
    ans = True;
    return ans;

def nqueens(l):
    ans = True
    i = 0
    while i < len(l) and ans:
        j = i + 1
        while j < len(l) and ans:
            flag = hor(l[i][0], l[j][0]) and ver(l[i][1], l[j][1]) and diag(l[i][0], l[i][1], l[j][0], l[j][1])
        
    return ans

def configurations(n):
    ans = comb(n*n, n)
    return ans

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
        pos = "Yes" if nqueens(l) else "No"
        config = configurations(n)
        num = str(config) if config <= 1000000000000 else sn_format(n)
        print("Case ", i + 1, ":", sep="")
        print("Satisfies ", n, "-queen(s) problem? -> ", pos, sep="")
        print("Total Possible Configurations for ", n, "-queen(s): ", num, " configurations", sep="")
    return 0

main()
