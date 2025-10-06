def calculate():
    n = int(input())
    vals = list(map(int,input().split()))

    mA = -float("inf")
    mB = float("inf")
    ts = 0

    for i in range(n):
        if (i+1)%2 == 0:
            if mA < vals[i]:
                mA = vals[i]
            ts -= vals[i]
        else:
            if mB > vals[i]:
                mB = vals[i]
            ts += vals[i]
            
    
    if mA > mB:
        ts += 2 * (mA - mB)

    print(ts)

if __name__ ==  "__main__":
    calculate()