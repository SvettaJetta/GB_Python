import csv
import logging
import pandas as pd

from Model.User import User

logging.basicConfig(filename='book.log', level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%H:%M:%S ' '%d.%m.%Y ')

class Book():
    _book_name:str = "address_book"
    _id = 0

    def __init__(self):
        pass


    def init(self):
        with open(f'{self._book_name}.csv', 'w+', encoding='utf-8', newline="\n") as csvfile:

            writer = csv.writer(csvfile)
            field_names = ['id', 'last_name', 'first_name', 'phone', 'about']
            writer.writerow(field_names)

            logging.info(f'Address Book created with name {self._book_name}')


    def insert(self, user:User):
        with open(f'{self._book_name}.csv', 'r', encoding='utf-8', newline="\n") as csvfile:
            final_line = csvfile.readlines()[-1]
            self._id = int(final_line.split(",")[0]) + 1
        with open(f'{self._book_name}.csv', 'a', encoding='utf-8', newline="\n") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self._id,user.last_name,user.first_name,user.phone,user.about])
        logging.info(f'User {user.first_name}  added ')
        return 0

    def delete(self, user:User.id):
        df = pd.read_csv(f'{self._book_name}.csv',index_col=0)

        df.set_index('id', inplace=True)

        df.drop(user)
        df.to_csv(f'{self._book_name}.csv')
        return 0


    def search(self, quary:str):
        with open(f'{self._book_name}.csv', 'r', encoding='utf-8', newline="\n") as csvfile:
            reader = csv.DictReader(csvfile)
            view = []
            for row in reader:
                if (row['last_name'] == quary) or (row['first_name'] == quary) or row['phone'] == quary:
                    view.append(
                        row
                    )

        #print(view)
        return view


        return 0

    def view(self):
        with open(f'{self._book_name}.csv', 'r', encoding='utf-8', newline="\n") as csvfile:
            reader = csv.DictReader(csvfile)
            view = []
            for row in reader:
                view.append(row)
        return view


