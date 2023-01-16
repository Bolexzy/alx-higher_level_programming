#!/usr/bin/python3
"""Defines a rectangle class model."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.

        Raises:
            TypeError: If either of width or height is not an int.
                        If either of x or y is not an int.
            ValueError: If either of width or height <= 0.
                        If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set/get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """Set/get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Returns the area value of the rectangle instance."""
        return (self.__width * self.__height)

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print() for y in range(self.y)]

        for i in range(self.height):
            [print(' ' * self.x, end='')]
            print('#' * self.width)

    def update(self, *args, **kwargs):
        """Update the attributes  of the rectangle.
        Args:
            *args (ints): New attributes values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        args_list = list(args)
        valid_keys = ['y', 'x', 'width', 'height']

        if (kwargs and len(kwargs) != 0):
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

        elif (args and len(args) != 0):
            for a in range(len(args_list)):
                if a == 0:
                    if args_list[a] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args_list[a]
                elif a == 1:
                    self.width = args_list[a]
                elif a == 2:
                    self.height = args_list[a]
                elif a == 3:
                    self.x = args_list[a]
                elif a == 4:
                    self.y = args_list[a]

    def to_dictionary(self):
        """Return the dictionary representaion of a Rectangle."""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
            }

    def __str__(self):
        """Return the str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
