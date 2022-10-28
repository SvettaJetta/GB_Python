import random as rnd
class Player_bot:
    __candy: int
    __tic: str

    def __init__(self):
        pass

    def candy(self, candy):
        self.__candy = candy
        if candy<=28and candy !=0:
            return candy
        else:
            candy = rnd.randint(1, 28)
        return candy
    def tic_tac(self, tic):
        self.__tic = tic
        return [rnd.randint(0,2),rnd.randint(0,2),tic]

def candy_games(candy=2021):
    player1 = Player_bot()
    player2 = Player_bot()
    while(candy>0):
        can = player1.candy(candy)
        candy -= can
        if candy == 0:
            print(f'player 01 - winner')
        else:
            print(f"p1 put {can}, {candy} is left")


        can = player2.candy(candy)
        candy -= can
        if candy == 0:
            print(f'player 02 - winner')
        else:
            print(f"p2 put {can}, {candy} is left")





def tic_tac_toe():
    field = [[1,2 ,3 ],
             [4, 5, 6],
             [7, 8, 9]]
    win = True
    while(win):

        pl1 = Player_bot().tic_tac("x")
        if type(field[pl1[0]][pl1[1]])!=type(''):
            field[pl1[0]][pl1[1]] = pl1[2]


        pl2 = Player_bot().tic_tac("O")
        if type(field[pl2[0]][pl2[1]])!=type(''):
            field[pl2[0]][pl2[1]] = pl2[2]

        if field[0][0] == field[0][1] == field[0][2] or field[1][0] == field[1][1] == field[1][2] or field[2][0] == \
                field[2][1] == field[2][2] or field[0][0] == field[1][0] == field[2][0] or field[0][1] == field[1][1] == \
                field[2][1] or field[0][2] == field[1][2] == field[2][2] or field[0][0] == field[1][1] == field[2][2] or \
                field[0][2] == field[1][1] == field[2][0]:
            for i in range(0, 3):
                for j in range(0, 3):
                    if type(field[i][j]) == type(0):
                        field[i][j] = ''
            for f in field:
                print(f)
            win = False
        pass


def encode(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string

def decode(message):
    decoded_message = ""
    i = 0
    j = 0

    while (i <= len(message) - 1):
        run_count = int(message[i])
        run_word = message[i + 1]
        for j in range(run_count):
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message


def lre_display():
    encoded_message=""
    with open("message.txt","r",encoding='utf-8') as f_mess:
        text = f_mess.readlines()
        for x in text:
            message = encode(x)

    with open("out.txt","w",encoding='utf-8') as f_out:
        f_out.writelines(message)

    decode_text = open("out.txt", "r", encoding='utf-8')
    lines = decode_text.readlines()
    for line in lines:
        print(line)
        print(decode(line))



if __name__ == '__main__':
    print("################# Task 1 ###############")
    candy_games()
    print("################# Task 2 ###############")
    tic_tac_toe()
    print("################# Task 3 ###############")
    lre_display()



