def check():
    n, m = map(int, input().split())

    if n % 10 == 0:
        print(n)
        return

    for _ in range(min(m, 10)):
        last = n % 10
        if last == 0:
            break
        n += last
        m -= 1

    if n % 10 == 0:
        n += 10 * m

    print(n)


if __name__ == "__main__":
    check()
