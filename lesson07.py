import logging
import os
import sympy as sym

NUMBER_TYPE = {
    1: "Rational",
    2: "Complex",
    0: "Exit"
}

OPERATIONS_NUMBER = {
    1: "Plus",
    2: "Multiplication",
    3: "Division",
    4: "Subtraction",
    0: "Exit"
}

logging.basicConfig(filename = "mylog.log")
def logger(a, b, operant):
    logging.info(f"The values of a and b are {a} and {b}.")
    try:
        logging.info(f"a, b successful with operator {operant}.")
    except ZeroDivisionError as err:
        logging.error("ZeroDivisionError", exc_info=True)


def rational_operation(selected_operator,selected_type):
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

        if selected_operator == "plus":
            return plus(a, b, selected_type)
        if selected_operator == "multiplication":
            return multiplication(a, b, selected_type)
        if selected_operator == "division":
            return division(a, b, selected_type)
        if selected_operator == "subtraction":
            return subtraction(a, b, selected_type)

        else:
            rational_operation(selected_operator,selected_type)

        logger(a, b, selected_operator)

def complex_operation(selected_operator, selected_type):
    if selected_operator == "exit":
        exit()
    else:
        global a, b
        try:
            a = str(input("(1)Enter complex nummber like a a,b: ")).split(",")
            b = str(input("(2)Enter complex nummber like a a,b: ")).split(",")

        except:
            print("")
            rational_operation(selected_operator,selected_type)

        if selected_operator == "plus":
            return plus(a, b, selected_type)
        if selected_operator == "multiplication":
            return multiplication(a, b, selected_type)
        if selected_operator == "division":
            return division(a, b, selected_type)
        if selected_operator == "subtraction":
            return subtraction(a, b, selected_type)
        if selected_operator == "exit":
            exit()
        else:
            complex_operation(selected_operator, selected_type)

        logger(a, b, selected_operator )


def plus(a, b, op):
    global result
    if op == "complex":
        return complex(int(a[0]), int(a[1])) + complex(int(b[0]), int(b[1]))
    if op == "rational":
        return sym.Rational(int(a[0]), int(a[1])) + sym.Rational(int(b[0]), int(b[1]))




def multiplication(a, b, op):
    global result
    if op == "complex":
        return complex(int(a[0]), int(a[1])) * complex(int(b[0]), int(b[1]))
    if op == "rational":
        return sym.Rational(int(a[0]), int(a[1])) * sym.Rational(int(b[0]), int(b[1]))




def division(a, b, op):
    global result
    if op == "complex":
        return  complex(int(a[0]), int(a[1])) / complex(int(b[0]), int(b[1]))
    if op == "rational":
        return  sym.Rational(int(a[0]), int(a[1])) / sym.Rational(int(b[0]), int(b[1]))



def subtraction(a, b, op):
    global result
    if op == "complex":
        return complex(int(a[0]), int(a[1])) - complex(int(b[0]), int(b[1]))
    if op == "rational":
        return sym.Rational(int(a[0]), int(a[1])) - sym.Rational(int(b[0]), int(b[1]))



def print_operations():
    print("Operations Menu")
    for x in OPERATIONS_NUMBER:
        print('\t', x, OPERATIONS_NUMBER[x])
    selected_operator = int(input("Input operator: "))

    return str(OPERATIONS_NUMBER[selected_operator]).lower()


def print_types():
    print("Types Menu")
    for x in NUMBER_TYPE:
        print('\t', x, NUMBER_TYPE[x])
    selected_type = int(input("Input Type: "))

    return str(NUMBER_TYPE[selected_type]).lower()


def menu():
    selected_type = print_types()
    print("Selected type is: ",selected_type)

    if selected_type == "rational":
        my_operator = print_operations()
        print("Operator: ", my_operator)
        print(rational_operation(my_operator, selected_type))

    if selected_type == "complex":
        my_operator = print_operations()
        print("Operator: ", my_operator)
        print(complex_operation(my_operator, selected_type))

    if selected_type == "exit":
        exit()
    else:
        print("")
        # menu()


if __name__ == '__main__':
    menu()
