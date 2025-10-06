
def max_contest():
    n,m = map(int,input().split())
    d = list(map(int,input().split()))
    letters = dict()
    lt = list()
    if n == m:
        print(" ".join(map(str,d)))
        return 
    for i in d:
        if i not in letters:
            letters[i] = 0
            lt.append(i)
        else :
            letters[i] += 1
    for s in letters.keys():
        k = len(lt)
        if letters[s] > 0:
            if letters[s] >= (m-k):
                lt.extend(([s] * (m-k)))
            else:
                lt.extend(([s]  * letters[s]))
        if k >= m:
            print(" ".join(map(str,lt[:m])))
            return

if __name__ == "__main__":
    max_contest()
