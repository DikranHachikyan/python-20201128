
# 1. дефиниция на класа
class Point:
    # данни на класа (статична променлива)
    label = 'A'
    # Конструктор на класа  
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('object constructor')
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

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # p1 - обект, Point - клас    
    p1 = Point(0, 45)
    p2 = Point(5,8)

    p1.z = 100 # динамичен атрибут
    
    Point.label = 'P'
    # p1.label = 'XX' маскира label на ниво клас!!! 
    print(f'label:{p1.label} p1({p1._x}, {p1._y}, {p1.z})')
    #AttributeError
    # print(f'label:{p2.label} p2:({p2._x}, {p2._y}, {p2.z})')
    print(f'label:{p2.label} p2:({p2._x}, {p2._y})')
    