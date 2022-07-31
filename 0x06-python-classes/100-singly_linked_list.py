#!/usr/bin/python3


class Node:
    ''' node of a singly linked list
    '''
    def __init__(self, data, next_node=None):
        ''' initialized a node
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        ''' method that returns the data of a node
        '''
        return self.__data

    @data.setter
    def data(self, value):
        ''' method that sets the data of a node
        '''
        if isinstance(value, int) is False:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        ''' method that returns the next node
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        ''' method that sets the next node
        '''
        if value is not None and isinstance(value, Node) is False:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    ''' a singly linked list
    '''
    def __init__(self):
        ''' initializes a singly linked list
        '''
        self.__head = None

    def sorted_insert(self, value):
        ''' method that inserts a node into a linked list
        '''
        if self.__head is None:
            self.__head = Node(value, None)
        elif value <= self.__head.data:
            new = Node(value, self.__head)
            self.__head = new
        else:
            ptr = self.__head
            while ptr.next_node is not None and ptr.next_node.data <= value:
                ptr = ptr.next_node

            tmp = ptr.next_node
            ptr.next_node = Node(value, tmp)

    def __str__(self):
        ''' the printable representation of the linked list
        '''
        ptr = self.__head
        toprint = ''
        while ptr is not None:
            toprint = toprint + str(ptr.data) + '\n'
            ptr = ptr.next_node
        return toprint[:-1]
