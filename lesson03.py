def task01(list):
    result = 0
    for x in range(1, len(list), 2):
        result += list[x]
    return result


def task02(list):
    result = []
    pos = len(list) - 1
    lenght = len(list)
    if lenght % 2 == 0:
        for x in range(0, lenght // 2):
            result.append(list[x] * list[pos])
            pos -= 1
    else:
        for x in range(0, (lenght // 2) + 1):
            result.append(list[x] * list[pos])
            pos -= 1
    return result


def task03(list):
    max = round(list[0] % 1, 3)
    min = round(list[0] % 1, 3)

    for x in range(1, len(list)):
        if max < round(list[x] % 1, 3): max = round(list[x] % 1, 3)
        if min > round(list[x] % 1, 3) != 0: min = round(list[x] % 1, 3)

    return max - min


def task04(value):
    return format(value, 'b')


def task05(n):
    fibonachchi = []

    fibonachchi_right_side = []
    fibonachchi_right_side.append(0)
    fibonachchi_right_side.append(1)

    fibonachchi_left_side = []
    fibonachchi_left_side.append(1)
    fibonachchi_left_side.append(-1)

    for x in range(2, n + 1):
        fibonachchi_right_side.append(fibonachchi_right_side[x - 1] + fibonachchi_right_side[x - 2])

    for x in range(2, n):
        fibonachchi_left_side.append(fibonachchi_left_side[x - 2] - fibonachchi_left_side[x - 1])

    fibonachchi_left_side.reverse()

    fibonachchi.extend(fibonachchi_left_side)
    fibonachchi.extend(fibonachchi_right_side)

    return fibonachchi


if __name__ == '__main__':
    print("################# Task 1 ###############")
    print(task01(list=[2, 3, 5, 9, 3]))
    print("################# Task 2 ###############")
    print(task02(list=[2, 3, 4, 5, 6]))
    print("################# Task 3 ###############")
    print(task03(list=[1.1, 1.2, 3.1, 5, 10.01]))
    print("################# Task 4 ###############")
    print(task04(10))
    print("################# Task 5 ###############")
    print(task05(8))
