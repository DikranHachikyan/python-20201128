from math import sqrt

class A:
    pass

# 1. дефиниция на класа
class Point:
    '''Class Point'''
    # данни на класа (статична променлива)
    label = 'A'
    # Конструктор на класа  
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print(f'object constructor ({x}, {y})')
        # Данни на обекта
        self._x = x
        self._y = y
        Point.label = 'M'

    # Методи на класа
    def draw(self):
        print(f'draw point at:({self._x}, {self._y})')

    def move_to(self,dx,dy):
        self._x += dx
        self._y += dy
    # Специални методи
    # function override
    def __str__(self):
        return f'({self._x},{self._y})'

    def __add__(self,other):
        # self - данните на левия операнд
        # other - данните на десния операнд
        # 1
        # assert isinstance(other, Point), 'right operand must be Point'

        if isinstance(other, Point):
            new_x = self._x + other._x 
            new_y = self._y + other._y
        elif isinstance(other, (int, float)):
            new_x = self._x + other 
            new_y = self._y + other
        else:
            # return NotImplemented
            raise NotImplementedError(f'not impelented yet')

        return Point(new_x, new_y)

    def __gt__(self, other):
        if isinstance(other, Point):
            dx1 = self._x ** 2
            dy1 = self._y ** 2
            dist1 = sqrt(dx1 + dy1)
            dx2 = other._x ** 2
            dy2 = other._y ** 2
            dist2 = sqrt(dx2 + dy2)
            return dist1 > dist2
        return NotImplemented 

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # p1 - обект, Point - клас    
    p1 = Point(7, 4)
    p2 = Point(5, 8)
    a = A()


    # s = str(p2)
    # print(s)

    p = p1 + p2
    print(f'point p{p}')

    # p = p1 + a

    p1 = p1 + 5.6

    p2 += 3

    if p2 > p1:
        print(f'{p2} > {p1}')
    else:
        print(f'{p2} <= {p1}')
    # elif p2 == p1:
    #     pass
