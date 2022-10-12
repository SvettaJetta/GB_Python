import math


class Poit:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def distance(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return math.hypot(dx, dy)


def task06(n):
    if 0 < n < 8:
        if 5 < n < 8:
            print("yes")
        else:
            print("no")
    else:
        print("something wrong")
        task06()


def task07():
    base = [[0, 0, 0],
            [0, 0, 1],
            [0, 1, 0],
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 1]]

    for logic in base:
        x = logic[0]
        y = logic[1]
        z = logic[2]

        logic_left = not (x or y or z)
        logic_right = (not x) and (not y) and (not z)
        if logic_left == logic_right:
            print(logic_left, "=", logic_right)
        else:
            print("something wrong")


def task08(x, y):
    point = Poit(x, y)
    if (point.x > 0) and (point.y > 0):
        print("1")
    if (point.x < 0) and (point.y > 0):
        print("2")
    if (point.x < 0) and (point.y < 0):
        print("3")
    if (point.x > 0) and (point.y < 0):
        print("4")
    if (point.x == 0) and (point.y == 0):
        print("something wrong")
        print(f'({point.x},{point.y}) is center')




def task09(quadrant):

    interval_positive = u'(0;+\u221E)'
    interval_negative = u'(-\u221E;0)'
    belong = u'\u2208'

    if quadrant == 1:
        print(u'x', belong, interval_positive)
        print(u'y', belong, interval_positive)
    elif quadrant == 2:
        print(u'x', belong, interval_negative)
        print(u'y', belong, interval_positive)
    elif quadrant == 3:
        print(u'x', belong, interval_negative)
        print(u'y', belong, interval_negative)
    elif quadrant == 4:
        print(u'x', belong, interval_positive)
        print(u'y', belong, interval_negative)
    else:
        print("something wrong")
        task09()


def task10(x1,y1,x2,y2):
    point1 = Poit(x1, y1)
    point2 = Poit(x2, y2)
    dist = Poit.distance(point1, point2)
    print(round(dist, 3))


if __name__ == "__main__":
    print("################# Task 6 ###############")
    n = int(input("Enter a day "))
    task06(n)

    print("################# Task 7 ###############")
    task07()

    print("################# Task 8 ###############")
    x = int(input("x="))
    y = int(input("y="))
    task08(x=x, y=y)

    print("################# Task 9 ###############")
    q = int(input("Enter a quadrant "))
    task09(q)

    print("################# Task 10 ###############")
    x1 = int(input("x1="))
    y1 = int(input("y1="))
    x2 = int(input("x2="))
    y2 = int(input("y2="))
    task10(x1, y1, x2, y2)