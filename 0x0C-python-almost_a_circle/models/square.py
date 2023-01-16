#!/usr/bin/python3
"""Defines a square class module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialiaze a new square
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes  of the square.
        Args:
            *args (ints): New attributes values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        args_list = list(args)

        if (kwargs and len(kwargs) != 0):
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

        elif (args and len(args) != 0):
            for a in range(len(args_list)):
                if a == 0:
                    if args_list[a] is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = args_list[a]
                elif a == 1:
                    self.size = args_list[a]
                elif a == 2:
                    self.x = args_list[a]
                elif a == 3:
                    self.y = args_list[a]

    def to_dictionary(self):
        """Return the dictionary representaion of a Square."""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
            }

    def __str__(self):
        """Return the string representation of the a Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.height)
