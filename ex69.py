
from draw import Point

class Rectangle(Point):
    
    def __init__(self, x = 0, y = 0, width = 0, height = 0, *args, **kwargs):
        super().__init__(x,y)
        print('Ctor Rectangle')
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def __str__(self):
        return super().__str__() + f'[{self.width}x{self.height}]' 

    def draw(self):
        super().draw()
        print(f'draw rect with:[{self.width}x{self.height}]')   

if __name__ == '__main__':
    r = Rectangle(3, 4, 100, 200)

    print(f'rectangle:{r}')

    r.draw()

    print(f'rectangle:({r.x},{r.y})[{r.width}x{r.height}]')