#!/usr/bin/python3


class Square:
    ''' class representing a square
    '''
    def __init__(self, size=0, position=(0, 0)):
        ''' method initializing a square of size size
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        ''' method that returns the size of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' method that sets the size of the square
        '''
        if isinstance(value, int) is False:
[O            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        ''' method that returns the position of the square
        '''
        return self.__position

    @position.setter
    def position(self, value):
        ''' method that sets the position of the square
        '''
        if isinstance(value, tuple) is False or len(value) != 2 or \
           type(value[0]) != int or type(value[1]) != int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        ''' method that returns area of the square
        '''
        return self.__size * self.__size

    def __str__(self):
        ''' printable representation of square
        '''
        toprint = ''
        if self.__size == 0:
            return toprint
        for a in range((self.__position)[1]):
            toprint = toprint + '\n'
        for i in range(self.__size):
            for b in range((self.__position)[0]):
                toprint = toprint + ' '
            for j in range(self.size):
                toprint = toprint + '#'
            toprint = toprint + '\n'
        return toprint[:-1]

    def my_print(self):
        ''' method that prints the square
        '''
        print(self)
