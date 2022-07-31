#!/usr/bin/python3
"""define class Square"""


class Square:
    """Defines a square:"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializer object"""

        self.__size = size
        self.__position = position

    def area(self):
        """return area of the Square in the atribute private __size"""

        return self.__size ** 2

    @property
    def size(self):
        """converts the private attribute self .__ size
        into a readable variable in the
        way self.size and in the same way as a public
        attribute it is modifiable.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """assigns the value to the size variable"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print a square with size of self.__size
        and if self.position[1] is greater than 0
        print a line break and if size is less
        than or equal to 0 print line break.
        """

        position = self.position[0]
        size = self.size
        [print('\n', end='') for _ in range(self.position[1])]

        for _ in range(self.size):
            for _ in range(position):
                print(' ', end='')
            print(size * '#')

    @property
    def position(self):
        """makes the private attribute self
        .__position a readable variable in
        the way self.position and in the same
        way that a public attribute is modifiable.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """assigns the value to the position variable"""

        if type(value) is not tuple or len(value) > 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value
