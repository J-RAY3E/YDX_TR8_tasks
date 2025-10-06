
def possible_passwords():
    n = list(input())
    letters = dict()
    l = 0
    for i in n:
        if i not in letters:
            letters[i] = 1
        else :
            letters[i] += 1
        l += 1
    sum_d = 0

    for i in letters.keys():
        if letters[i] > 1:
            sum_d += (letters[i] * (letters[i] - 1)) / 2

    total = (( l * (l-1) / 2) - sum_d) + 1

    print(int(total))

if __name__ == "__main__":
    possible_passwords()
