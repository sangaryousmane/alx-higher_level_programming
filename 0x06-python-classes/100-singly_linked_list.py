#!/usr/bin/python3
""" Handles the implementation of a node"""


class Node:
    """ Implement a node"""

    def __init__(self, data, next_node=None):
        """The constructor

        Args:
          data: store the node data
          next_node: holds the node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ our accessor method"""
        return self.__data

    @data.setter
    def data(self, value):
        """ Our mutator method for the data field"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ the accessor method for the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ the mutator method for the next node"""
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""This class mimicks a linked list"""


class SinglyLinkedList:
    """ Handles the mimicking of a linkedlist """

    def __init__(self):
        """ class constructor """
        self.__head = None

    def __str__(self):
        """print the linked list element"""

        to_string = ""
        temp = self.__head
        while temp:
            to_string += str(temp.data) + "\n"
            temp = temp.next_node
        return to_string[:-1]

    def sorted_insert(self, value):
        """ Insert in a sorted list"""

        new_node = Node(value)
        if not self.__head:
            self.__head = new_node
            return
        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        temp = self.__head
        while temp.next_node and temp.next_node.data < value:
            temp = temp.next_node

        if temp.next_node:
            new_node.next_node = temp.next_node
        temp.next_node = new_node
