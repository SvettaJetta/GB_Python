from math import sqrt, pow
import random as rnd

def task_with_files():
    with open("users.txt","r",encoding='utf-8') as f_users:
        users = f_users.read().splitlines()

    with open("hobby.txt","r",encoding='utf-8') as f_hobby:
        hobbys = f_hobby.read().splitlines()

    users_hobby = open("users_hobby", "a", encoding='utf-8')
    for user, hobby in zip(users, hobbys):
        users_hobby.writelines(user +" - "+hobby+"\n")
    users_hobby.close()


def PI(d=0.001):
    d = int(1 / d)
    sep = len(str(d)) - 2
    product = 1
    for k in range(1, d):
        p = pow(k, 2) / (pow(k, 2) - pow(1 / 3, 2))
        product *= p

    pi = round(3 * (sqrt(3) / 2) * product, sep)

    return pi


def simple_multiples(n):
    k = 2
    list = []
    while k <= n:
        if n % k == 0:
            list.append(k)
            n /= k
        else:
            k += 1

    return list


def non_repeating_elements(list=[4, 2, 6, 1, 2, 4, 1, 6, 3, 7, 2]):
    nonrepeating = []
    for x in list:
        if list.count(x) == 1:
            nonrepeating.append(x)
    return nonrepeating


def factors(n):
    arguments = []
    polynom = ''
    result = open("result.txt", mode="w+")

    for m in range(n, -1, -1):
        if m == n:
            a = rnd.randint(1, 100)
            arguments.append(a)
            if a == 1.0:
                polynom = f'x^{m}'
            else:
                polynom = f'{a}x^{m}'


        elif m == 0:
            a = rnd.randint(0, 100)
            arguments.append(a)
            if a != 0.0:
                polynom += f'+{a}'

        elif m == 1:
            a = rnd.randint(0, 100)
            arguments.append(a)

            if a == 0.0:
                polynom += f''
            elif a == 1.0:
                polynom += f'+x'
            else:
                polynom += f'+{a}x'

        else:
            a = rnd.randint(0, 100)
            arguments.append(a)

            if a == 0:
                polynom += f''
            elif a == 1.0:
                polynom += f'+x^{m}'
            else:
                polynom += f'+{a}x^{m}'

    print(arguments)
    print(polynom + "=0")

    arguments = str(arguments)
    result.writelines(arguments+"\n")
    result.writelines(polynom+"=0")
    result.close()




if __name__ == '__main__':
    print("################# Task pi ###############")
    print(PI())
    print("################# Task 30 ###############")
    task_with_files()
    print("################# Task 31 ###############")
    print(simple_multiples(528))
    print("################# Task 32 ###############")
    print(non_repeating_elements([4, 2, 3, 7, 2]))
    print("################# Task 33 ###############")
    factors(7)