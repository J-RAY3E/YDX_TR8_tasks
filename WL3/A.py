def det():
    n = int(input())
    dp = [0] * (n+1)

    def step(n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        
        if dp[n] > 0:
            return dp[n]
        dp[n] = step(n-1)  + step(n-2) + step(n-3)



        return dp[n]
        
    print(step(n))
if __name__ == "__main__":
    det()