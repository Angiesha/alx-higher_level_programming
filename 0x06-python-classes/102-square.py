#!/usr/bin/python3


class Square:
    ''' class representing a square
    '''
    def __init__(self, size=0):
        ''' method initializing a square of size size
        '''
        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def __lt__(self, other):
        ''' method for <
        '''
        if self.__size < other.__size:
            return True
        else:
            return False

    def __le__(self, other):
        ''' method for <=
        '''
        if self.__size <= other.__size:
            return True
        else:
            return False

    def __gt__(self, other):
        ''' method for >
        '''
        if self.__size > other.__size:
            return True
        else:
            return False

    def __ge__(self, other):
        ''' method for >=
        '''
        if self.__size >= other.__size:
            return True
        else:
            return False

    def __eq__(self, other):
        ''' method for ==
        '''
        if self.__size == other.__size:
            return True
        else:
            return False

    def __ne__(self, other):
        ''' method for !=
        '''
        if self.__size != other.__size:
            return True
        else:
            return False

    @property
    def size(self):
        ''' method that returns the size of the square
[O        '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' method that sets the size of the square
        '''
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        ''' method that returns area of the square
        '''
        return self.__size * self.__size
