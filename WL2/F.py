def max_diff():

    n,m = map(int,input().split())
    ls = [list(input()) for _ in range(n)]
    c = [0] * n
    r = [0] * m

    for i in range(n):
        for j in range(m):
            c_t = ls[i][j]
            if c_t == "?":
                c[i] +=  1
                r[j] -=  1
            elif  c_t == "+":
                c[i] +=  1
                r[j] +=  1
            else:
                c[i] -= 1
                r[j] -= 1

    ma = max(c)
    mi = min(r)
    x = [i for i in range(n) if c[i] == ma]
    y = [j for j in range(m) if r[j] == mi]

    for xi in x:
        for yi in y:

            if ls[xi][yi] != "?":
                print(ma-mi)
                return
        
    print(ma-mi-2)
if __name__ ==  "__main__":
    max_diff()