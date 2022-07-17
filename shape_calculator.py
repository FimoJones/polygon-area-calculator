class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        width = self.width
        height = self.height
        
        if width > 50 or height > 50:
            return 'Too big for picture.'

        return height * (width * '*' + '\n')
        
    def get_amount_inside(self, shape):
        width_fits = self.width // shape.width
        height_fits = self.height // shape.height

        return width_fits * height_fits
        
class Square(Rectangle):
    def __init__(self, side):
        self.width = self.height = side

    def __repr__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = self.height = side

    def set_width(self, width):
        self.width = self.height = width
    
    def set_height(self, height):
        self.width = self.height = height
