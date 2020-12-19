
# 1. дефиниция на класа
class Point:
    # Конструктор на класа  
    def __init__(self):
        print('object constructor')
        # Данни на класа
        self.x = 10
        self.y = 20

    # Методи на класа
    def draw(self):
        print(f'draw point at:({self.x}, {self.y})')

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # p1 - обект, Point - клас    
    p1 = Point()

    print(f'p1:({p1.x}, {p1.y})')

    p1.x = 15

    p1.draw()