def det():
    t = input()
    n = len(t)
    l = int(input())
    words = [input() for _ in range(l)]
    dp = [False] * (n+1)
    dp[0] = True
    prev =  [-1] * (n+1)
    
    for i in range(n):
        if not dp[i]:
            continue
        for word in words:
            if t.startswith(word,i):
                j = i + len(word)
                dp[j] = True
                prev[j] = i

    print(prev)
    res = []
    i = n
    while i > 0:
        j = prev[i]
        res.append(t[j:i])
        i = j

    print(" ".join(reversed(res)))

    

if __name__ == "__main__":
    det()