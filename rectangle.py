def rectangle(a, p):
    counter = 0
    s = 0
    n = len(a)
    for j in range(counter, n-1):
        for i in range(counter+1, n-1):
            area = a[counter]*a[i]
            if area % p != 0 and area > s:
                s = area
        counter += 1
    return s


if __name__ == '__main__':
    a1 = [7, 5, 11, 33]
    p1 = 3

    a2 = [15, 12, 10, 6, 5, 1]
    p2 = 5

    a3 = [6, 28, 7, 12, 10, 14, 5, 9, 4, 8, 18]
    p3 = 7

    a4 = [4, 34, 16, 8, 6, 22, 14, 12, 2, 7]
    p4 = 2

    a = rectangle(a1, p1)
    b = rectangle(a2, p2)
    c = rectangle(a3, p3)
    d = rectangle(a4, p4)

    print(f'{a}, {b}, {c}, {d}')