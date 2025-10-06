def check():

    n,m = map(int,input().split())
    s = input()
    ws = dict()
    for i in range(m):
        x = input()
        if x not in ws:
            ws[x] = [i]
        else:
            ws[x].append(i)
    
    sl = []
    sep = n//m
    for t in range(0,n,sep):
        sa  = s[t:t+sep]
        if sa in ws:
            if len(ws[sa]) == 0:
                break
            sl.append(ws[sa].pop()+1)
        else:
            break

    if len(sl) == m:
        print(" ".join(map(str, sl)))


if __name__ ==  "__main__":
    check()