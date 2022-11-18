import logging
import os
import sympy as sym


NUMBER_TYPE = {
    "Rational": 1,
    "Complex": 2,
    "Exit": 0
}

OPERATIONS_NUMBER = {
    "Plus": 1,  # Сложение
    "Multiplication": 2,  # Умножение
    "Division": 3,  # Деление
    "Subtraction": 4,  # Вычитание
    "Exit": 0
}


def logger(a, b, operant):
    logging.info(f"The values of a and b are {a} and {b}.")
    try:
        logging.info(f"a, b successful with result.")
    except ZeroDivisionError as err:
        logging.error("ZeroDivisionError", exc_info=True)


def rational_operation(selected_operator):
    # numerator = int(input("Numerator is:"))
    # denominator = int(input("Denominator is:"))

    if selected_operator == ("0" or "exit"):
        exit()
    else:
        global a, b
        try:
            a = str(input("(1)Enter Numerator and Denominator like a a/b: ")).split("/")
            b = str(input("(2)Enter Numerator and Denominator like a a/b: ")).split("/")

        except:
            print("")
            rational_operation(selected_operator)

        if selected_operator == ("1" or "+" or "plus"):
            return plus(a, b,selected_operator)
        if selected_operator == ("2" or "*" or "multiplication"):
            return multiplication(a, b,selected_operator)
        if selected_operator == ("3" or "/" or "Division"):
            return division(a, b,selected_operator)
        if selected_operator == ("4" or "-" or "subtraction"):
            return subtraction(a, b, selected_operator)

        else:
            rational_operation(selected_operator)




def complex_operation(selected_operator):

    if selected_operator == "0" or "exit":
        exit()
    else:
        global a, b
        try:
            a = str(input("(1)Enter complex nummber like a a,b: ")).split(",")
            b = str(input("(2)Enter complex nummber like a a,b: ")).split(",")

        except:
            print("")
            rational_operation(selected_operator)



        if selected_operator == ("1" or "+" or "plus"):
            return plus(a, b,selected_operator)
        if selected_operator == ("2" or "*" or "multiplication"):
            return multiplication(a, b,selected_operator)
        if selected_operator == ("3" or "/" or "division"):
            return division(a, b,selected_operator)
        if selected_operator == ("4" or "-" or "subtraction"):
            return subtraction(a, b,selected_operator)
        if selected_operator == ("0" or "exit"):
            exit()
        else:
            complex_operation(selected_operator)

        logger(a,b , selected_operator)


def plus(a, b, op):
    global result
    if op == ("2" or "complex"):
        result = complex(int(a[0]),int(a[1]))+complex(int(b[0]),int(b[1]))
    if op == ("1" or "rational"):
        result = sym.Rational(int(a[0]), int(a[1])) + sym.Rational(int(b[0]), int(b[1]))
    return result


def multiplication(a, b, op):
    global result
    if op == ("2" or "complex"):
        result = complex(int(a[0]),int(a[1]))*complex(int(b[0]),int(b[1]))
    if op == ("1" or "rational"):
        result = sym.Rational(int(a[0]), int(a[1])) * sym.Rational(int(b[0]), int(b[1]))

    return result


def division(a, b, op):
    global result
    if op == ("2" or "complex"):
        result =complex(int(a[0]),int(a[1]))/complex(int(b[0]),int(b[1]))
    if op == ("1" or "rational"):
        result = sym.Rational(int(a[0]), int(a[1])) / sym.Rational(int(b[0]), int(b[1]))
    return result


def subtraction(a, b, op):
    global result
    if op == ("2" or "complex"):
        result = complex(int(a[0]),int(a[1]))-complex(int(b[0]),int(b[1]))
    if op == ("1" or "rational"):
        result = sym.Rational(int(a[0]), int(a[1])) - sym.Rational(int(b[0]), int(b[1]))
    return result


def print_operations():
    print("Operations Menu")
    for x in OPERATIONS_NUMBER:
        print('\t', OPERATIONS_NUMBER[x], x)
    selected_operator = input("Input operator: ")

    return selected_operator.lower()


def print_types():
    print("Types Menu")
    for x in NUMBER_TYPE:
        print('\t', NUMBER_TYPE[x], x)
    selected_type = input("Input Type: ")

    return selected_type.lower()

def menu():
    selected_type = print_types()


    if selected_type == ("1" or "rational"):
        my_operator = print_operations()
        print(rational_operation(my_operator))


    if selected_type == ("2" or "complex"):
        my_operator = print_operations()
        print(complex_operation(my_operator))

    if selected_type == ("0" or "exit"):
        exit()
    else:
        print("")
        #menu()


if __name__ == '__main__':
    menu()
