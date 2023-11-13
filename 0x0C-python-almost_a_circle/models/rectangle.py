#!/usr/bin/python3
""" define class Rectangle """

from models.base import Base


class Rectangle(Base):
    """  class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """  super lets me call the constructor of base and set
            an id for every instance that is made from class Rectangle
            and every other child class of base
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


    #set a setter/getter for every private attribute
    #to be able to validate what a developer is trying to assign to a variable

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return (self.__height * self.__width)

    def display(self):
        """Print the rectangle with the # character."""
        [print("") for i in range(0, self.__y)]
        for row in range(0, self.__height):
            [print(" ", end="") for j in range(0, self.__x)]
            for column in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """String representation of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        #you can turn kwargs into a list of values
        
        if args and len(args) >= 1:
        # Update id using the first positional argument
            super().__init__(args[0])
        elif kwargs and 'id' in kwargs:
        # Update id using the 'id' keyword argument
            super().__init__(kwargs['id'])

        if args and len(args) >= 2:
            self.__width = args[1]
        elif kwargs and 'width' in kwargs:
            self.__width = kwargs['width']

        if args and len(args) >= 3:
            self.__height = args[2]
        elif kwargs and 'height' in kwargs:
            self.__height = kwargs['height']

        if args and len(args) >= 4:
            self.__x = args[3]
        elif kwargs and 'x' in kwargs:
            self.__x = kwargs['x']

        if args and len(args) >= 5:
            self.__y = args[4]
        elif kwargs and 'y' in kwargs:
            self.__y = kwargs['y']
