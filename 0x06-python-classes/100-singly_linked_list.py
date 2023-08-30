#!/usr/bin/python3
"""Module singly-linked list class."""
class Node:
    """Defines a node in a singly-linked list."""
    def __init__(self, data, next_node=None):
        """constructor.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
         """Get/set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly-linked list."""
    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.head = None

    def __str__(self):
        """Define the print() rep of a SinglyLinkedList."""
        res = ""
        node = self.head
        while node:
            res += str(node.data) + "\n"
            node = node.next_node
        return res[:-1]


    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        Args:
            value (Node): The new Node to insert.
        """

        new = Node(value)

        if not self.head:
            self.head = new
            return

        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        if node.next_node:
            new.next_node = node.next_node
        node.next_node = new
