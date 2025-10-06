def calculate_min_time():
    a, b, c, v0, v1, v2 = map(float, input().split())
    
    time1 = a / v0 + c / v1 + b / v2
    time2 = b / v0 + c / v1 + a / v2
    time3 = a / v0 + a / v1 + b / v0 + b / v1
    time4 = b / v0 + b / v1 + a / v0 + a / v1
    time5 = a / v0 + c / v1 + c / v2 + a / v1
    time6 = b / v0 + c / v1 + c / v2 + b / v2

    min_time = min(time1, time2, time3, time4, time5,time6)
    

    print("{:.15f}".format(min_time))

if __name__ == "__main__":
    calculate_min_time()