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
        self.x = x
        self.y = y
        Point.label = 'M'

    # Методи на класа
    def draw(self):
        print(f'draw point at:({self.x}, {self.y})')

    def move_to(self,dx,dy):
        self.x += dx
        self.y += dy
    # Специални методи
    # function override
    def __str__(self):
        return f'({self.x},{self.y})'

    def __add__(self,other):
        # self - данните на левия операнд
        # other - данните на десния операнд
        # 1
        # assert isinstance(other, Point), 'right operand must be Point'

        if isinstance(other, Point):
            new_x = self.x + other.x 
            new_y = self.y + other.y
        elif isinstance(other, (int, float)):
            new_x = self.x + other 
            new_y = self.y + other
        else:
            # return NotImplemented
            raise NotImplementedError(f'not impelented yet')

        return Point(new_x, new_y)

    def __gt__(self, other):
        if isinstance(other, Point):
            dx1 = self.x ** 2
            dy1 = self.y ** 2
            dist1 = sqrt(dx1 + dy1)
            dx2 = other.x ** 2
            dy2 = other.y ** 2
            dist2 = sqrt(dx2 + dy2)
            return dist1 > dist2
        return NotImplemented

    @property
    def x(self):
        return self._x #!! тук остава _x

    @x.setter
    def x(self, x):
        assert x >= 0, 'x must be positive'
        self._x = x #!! тук остава _x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        assert y >= 0, 'y must be positive'
        self._y = y

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # p1 - обект, Point - клас    
    p1 = Point(7, 4)
    p2 = Point(-17, -14)

    p1.x = 10
    p1.y = 12
    print(f'p1 : {p1}')    
    print(f'p2 : {p2}')    