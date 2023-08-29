#!/usr/bin/python3

class Square:

    def __str__(self):


        return self.my_sprint()[:-1]

    def __init__(self, size=0, position=(0, 0)):


        self.size = size
        self.position = position

    @property
    def size(self):


        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):


        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
         len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):

        return self.__size ** 2

    def my_sprint(self):

        res = ""
        if not self.size:
            return "\n"

        for i in range(self.position[1]):
                res += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                res += " "
            for j in range(self.size):
                res += "#"
            res += "\n"
        return res

    def my_print(self):

        print(self.my_sprint(), end="")
