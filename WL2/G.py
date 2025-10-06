def sequently_five():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            cc = s[i][j]
            if cc == ".":
                continue
                
            if m - j >= 5:
                result = [s[i][j+t] for t in range(5)]
                if all(x == cc for x in result):
                    print("Yes")
                    return
            
            if n - i >= 5:
                result = [s[i+t][j] for t in range(5)]
                if all(x == cc for x in result):
                    print("Yes")
                    return
            
            if n - i >= 5 and m - j >= 5:
                result = [s[i+t][j+t] for t in range(5)]
                if all(x == cc for x in result):
                    print("Yes")
                    return
            
            if n - i >= 5 and j >= 4:
                result = [s[i+t][j-t] for t in range(5)]
                if all(x == cc for x in result):
                    print("Yes")
                    return
                    
    print("No")

if __name__ == "__main__":
    sequently_five()