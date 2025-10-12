'''
def calculate_total():
    A,B,C,D = map(int,input().split())

    if B >= D:
        return A
    return  A + C * (D-B)


print(calculate_total())
'''
"""
import math 
def minimal_time():
    n,t = map(int,input().split())
    floors = list(map(int,input().split()))
    s = int(input())-1
    minfloor = floors[0]
    maxfloor = floors[-1]
    target_floor = floors[s]
    ans = 0

    if ((target_floor - minfloor) <= t) or ((maxfloor- target_floor) <= t) :
        ans = maxfloor - minfloor
    else:
        ans =  min ((maxfloor-target_floor)*2 + (target_floor - minfloor),
            (maxfloor-target_floor)+ (target_floor - minfloor)*2)

    return  ans

print(minimal_time())
"""
"""
def fib(n,fibs=None):
    # put your code here
    fibs = [-1]*(n+1) if fibs == None else fibs
    if n == 0:
        fibs[0] = 0
        return 0
    if n == 1:
        fibs[1] = 1
        return 1
    if fibs[n] != -1:
        return fibs[n]
    fibs[n] = fib(n-2,fibs) + fib(n-1,fibs)
    return fibs[n]
    
    
    

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()

"""
"""
def fib_digit(n):
    fibs = [0] * (n+1)
    for i in range(1,n+1,1):
        if i == 1:
            fibs[i] = 1
            continue
        a = int(str(fibs[i-1])[-1])
        b = int(str(fibs[i-2])[-1])
        fibs[i] = (a+b)%10
    return fibs[n]
def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()

"""
"""
def fib_mod(n, m):
    a = 0
    b = 1
    for _ in range(2,n+1,1):
        b,a = a+b,b
    return b%m
def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
"""
"""
def max_sum(arr,k):
    numbers = []
    t_empy = 0
    while t_empy  < len(arr):
        row = []
        t_empy = 0
        for number in arr:
            if len(number) == 0:
                t_empy += 1
                continue
            row.append(number.pop())
        if len(row) != 0:
            numbers.insert(0,row)

    l= len(numbers)-1

    ans = 0
    for t in numbers:
        for n in sorted(t):
            if n < 9:
                ans += (9-n) * 10**(l)
                k -= 1
            if k == 0:
                break 
        l -=  1
    return 0

if __name__ == "__main__":
    n,k = map(int,input().split())
    arr = [[int(d) for d in n] for n in input().split()]

    print(max_sum(arr,k))
"""
"""
def fib_mod(n, m):
    a = 0
    b = 1
    args = []
    for _ in range(2,n+1,1):
        b,a = a+b,b
        args.append(b%m)
    print(args)
    return b%m
def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()

"""

"""

def all_digits():
    l,m = input().split()
     
    mil = (len(l))
    mal = (len(m))
    brutal  = ((mal+1) - mil) * 9 
    t= 9

    while int(mal*str(t)) > int(m):
        brutal -= 1
        t -= 1
        if t == -1: break 
    t = 1
    while int(mil*str(t)) < int(l):
        brutal -= 1
        t += 1
        if t == 10: break

    return brutal
print(all_digits())

"""



def max_waste(n,days):
    day_l = []
    total = 0
    cupons  =  0
    for day in days:
        if day <= 100 and cupons == 0:
            total += day
        elif day > 100:
            cupons += 1
            total += day
        else:
            day_l.append(day)
    sd = sorted(day_l)
    while cupons > 0 and sd:
        sd.pop()
        cupons -= 1
    return total + sum(sd)
if __name__ == "__main__":
    n = int(input())
    days = []
    for _ in range(n):
        days.append(int(input()))
    print(max_waste(n,days))