import random as rnd


def task14(val) -> int:
    val = str(val)
    sum = 0
    for x in val:
        try:
            if x != ".":
                sum = sum + int(x)
        except:
            print('value have bad char')
    return sum


def task15(n) -> list:
    tmp = 1
    result_list = []
    for i in range(1, n + 1):
        result_list.append(i * tmp)
        tmp = i * tmp

    return result_list


def task16(n) -> dict:
    list = []
    for x in range(1, n + 1):
        list.append([x, round(pow((1 + (1 / x)), x), 2)])

    result = dict(list)
    return result


def task17(n, positions):
    if positions[0] < n and positions[1] < n:
        list = []
        product = 1
        for x in range(n):
            list.append(rnd.randint(-n, n))
        print(list)
        for y in positions:
            try:
                product = list[y] * product
            except:
                print("something wrong")
        print("product=", product)
    else:
        print("Жора все х%ня давай по новой")
        nn = int(input("N= "))
        p1 = int(input(f"p1 (val must be<{nn}!)= "))
        p2 = int(input(f"p2 (val must be<{nn}!)= "))
        task17(nn, positions=[p1, p2])


def task18(list):
    print(list)
    rnd.shuffle(list)
    print(list)


def task18_myshuffle(list):
    print(list)
    for x in list:
        position1 = rnd.randint(0, len(list) - 1)
        position2 = rnd.randint(0, len(list) - 1)
        temp = list[position1]
        list[position1] = list[position2]
        list[position2] = temp

    return list


if __name__ == "__main__":
    print("################# Task 14 ###############")
    value = float(input("Enter a value =  "))
    print("sum=", task14(value))

    print("################# Task 15 ###############")
    number = int(input("Enter a number =  "))
    print(task15(number))

    print("################# Task 16 ###############")
    num = int(input("N =  "))
    print(f"for n = {num}:{task15(num)}")

    print("################# Task 17 ###############")
    n = int(input("N = "))
    p1 = int(input(f"p1 = "))
    p2 = int(input(f"p2 = "))
    task17(n, positions=[p1, p2])

    print("################# Task 18 ###############")
    task18([2, 5, 7, 1, 2, 4])
    print("################# Task 18 ###############")
    print(task18_myshuffle([1, 2, 3, 4, 5, 6]))
