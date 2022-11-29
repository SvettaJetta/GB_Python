import csv
import logging
import os

from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *

from tabulate import tabulate

from Model.Book import Book as Book
from Model.User import User

logging.basicConfig(filename='book.log', level=logging.DEBUG, format='%(asctime)s %(message)s',
                    datefmt='%H:%M:%S ' '%d.%m.%Y ')

clear = lambda: os.system('cls')
book = Book()


def init():
    book.init()
    menu.prologue_text = "Book is inited"


def Add():
    print("Add to book")
    last_name = input("Last Name: ")
    name = input("First Name: ")
    phone = input("Phone: ")
    about = input("Description: ")
    user = User(last_name=last_name, first_name=name, phone=phone, about=about)

    book.insert(user)


def Del(val):
    book.delete(val)
    print(tabulate(book.view(), headers="keys", missingval="-", tablefmt="grid"))


def view():
    table = book.view()
    print(table)

    print(tabulate(table, headers="keys", missingval="-", tablefmt="grid"))


def Search(q):
    table = book.search(q)
    print(tabulate(table, headers="keys", missingval="-", tablefmt="grid"))

def menu():
    logging.info('Starting...')
    menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.HEAVY_BORDER) \
        .set_prompt("SELECT>") \
        .set_title_align('center') \
        .set_subtitle_align('center') \
        .set_left_margin(4) \
        .set_right_margin(4) \
        .show_header_bottom_border(True)

    menu = ConsoleMenu("Menu", "Phone Book", formatter=menu_format)

    itemInit = FunctionItem("Init", init)
    itemAdd = FunctionItem("Add", Add)
    itemDelete = FunctionItem("Delete", Del, args=[menu])

    itemSearch = FunctionItem("Search", Search, args=[menu])
    itemView = FunctionItem("View", view)

    menu.append_item(itemInit)
    menu.append_item(itemAdd)
    menu.append_item(itemDelete)
    menu.append_item((itemSearch))
    menu.append_item(itemView)

    clear()

    menu.start()
    menu.join()
    return menu


if __name__ == '__main__':
    menu()
