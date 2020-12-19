
# 1. дефиниция на класа
class Point:
    # Конструктор на класа  
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('object constructor')
        # Данни на класа
        self.__x = x
        self.__y = y

    # Методи на класа
    def draw(self):
        print(f'draw point at:({self.__x}, {self.__y})')

    def move_to(self,dx,dy):
        self.__x += dx
        self.__y += dy

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # p1 - обект, Point - клас    
    p1 = Point(0, 45)
    p2 = Point(30,40)

    print(f'p1:({p1.__x}, {p1.__y})')
    print(f'p2:({p2.__x}, {p2.__y})')

    p1.draw()
    p1.move_to(30, -5)
    p1.draw()