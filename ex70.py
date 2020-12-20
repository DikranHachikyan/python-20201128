
from draw import Rectangle, Point

def show():
    r = Rectangle()
    print(f'r:{r}')

if __name__ == '__main__':
    shapes = [Point(3,4), Rectangle(1,2,100,200), Point(7,8), Rectangle(4,5,120,300)]

    for shape in shapes:
        shape.move_to(10,20)
        shape.draw()
        print('-' * 20)