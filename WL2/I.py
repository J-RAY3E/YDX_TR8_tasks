def calculate_min_steps():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    total = 0 
    squares = abs(x2-x1) + abs(y2-y1)
    x2,y2 = x2-x1, y2-y1
    if x2 == 0 and y2 == 0:
        pass
    elif x2 == 0 or y2 == 0:
        total =  (squares-1) * 3
    else:
        total =  (squares-2) * 3 + 1

    print(total)


if  __name__ == "__main__":
    calculate_min_steps()