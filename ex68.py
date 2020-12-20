
# 1.
# import draw.point as drw 

# 2.
# без да използваме __init__.py
# from draw.point import Point
# или
# from draw.point import Point  as P
# p = P(1,2)

# 2.1
# с  __init__.py
from draw import Point

def show():
    p3 = Point(1,2)
    print(f'p3:{p3} (inst.:{Point.count})')
    p3.move_to(5,7)

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # p1 - обект, Point - клас    
    p1 = Point(7, 4)

    p1.x = 10
    p1.y = 12
    print(f'p1 : {p1} (ints:{Point.count})')

    p2 = Point(17, 14)
    print(f'p2 : {p2} (ints:{Point.count})') 
    show()  
    print(f'p1 : {p1} (ints:{Point.count})')    
    print(f'p2 : {p2} (ints:{Point.count})') 