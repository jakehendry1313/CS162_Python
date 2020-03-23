# Author:      Jacob Hendry
# Date:        02/19/2020
# Description: This is a python file called LinkedList.py. It will include two classes, Node and
#              LinkedList. The LinkedList class will have six different methods called add, remove,
#              display, insert, contains, and reverse.


class Node:
    """This is a class called Node. It will represent a node in a linked list and will
     initialize data members called data and next."""

    def __init__(self, data):
        """This is an init method that will initialize data members called data and next."""
        self.data = data
        self.next = None


class LinkedList:
    """This is a class called LinkedList. It will include six methods to add, remove, insert,
    find, display and reverse the nodes in the linked list."""

    def __init__(self):
        """This is a init method that will initialize a data member called head."""

        # Self.head will represent the beginning of the linked list
        self.head = None

    # Helper Function
    def add_rec(self, current, value):
        """This is a helper recursion function that will add a new node to the front of the linked list"""

        # If the list is empty, add the value to the list
        if current is None:
            return Node(value)

        # If the list is not empty, then add the value to the front of the list using recursion
        else:
            number = self.add_rec(current.next, value)
            current.next = number

            # Return the value to the add(value) method
            return current

    def add(self, value):
        """This is an add method that will add a given value to the linked list using a recursive
        helper function"""

        # The returned value will be in place of the self.head in the list
        self.head = self.add_rec(self.head, value)

    def display_rec(self, current):
        """This is a recursive helper function to display all of the values of each node in the linked
        list"""

        # If the list is empty, just return
        if current is None:
            return

        # If the list is not empty, return every value from the linked list
        else:

            # Print every value. The end value will print as an empty string
            print(current.data, end=" ")

            # Go to the next value in the list using recursion
            self.display_rec(current.next)

    def display(self):
        """This is a method called display that will use a helper function to display all of the values
        in each node of the linked list"""

        # Call the recursive function
        self.display_rec(self.head)
        print()

    def remove_rec(self, current, previous, value):
        """This is a recursive helper function to remove a single value from a node of the linked
        list"""

        # If the list is empty, return False because there exists no value
        if current is None:
            return False

        # If the value is in front of the list, continue
        if current.data == value:

            # If the previous value is None, the value is at the front
            if previous is None:

                # Now replace the next value with the current value to remove it
                self.head = self.head.next

            else:

                # If the value is inside the list, replace the next value to current to the previous next
                previous.next = current.next
                return True

        # Call the recursive remove_rec function to return the value
        return self.remove_rec(current.next, current, value)

    def remove(self, value):
        """This is a method called remove that will use a helper function to remove a node value from
        the linked list"""
        self.remove_rec(self.head, None, value)

    def contains_rec(self, current, value):
        """This is a recursive helper function that will determine if the given value is in the
        linked list"""

        # If the list is empty, return False
        if current is None:
            return False

        # If the current node is equal to the value, return True
        if current.data == value:
            return True

        # Call the recursive contains_rec function to find the value
        return self.contains_rec(current.next, value)

    def contains(self, value):
        """This is a method called contains that will use a helper function to find the given
        value"""

        # Return the True if the value is in the list and False if it is not
        return self.contains_rec(self.head, value)

    def insert_rec(self, current, previous, value, position):
        """This is a recursive helper function that will insert a given value into a position also
        given by the user"""

        # If the given position is zero, continue
        if position == 0:

            # If the previous value is None, continue:
            if previous is None:

                # Replace the front node value with the given value
                temp = self.head
                self.head = Node(value)
                self.head.next = temp

            else:
                # Replace the node value with the previous node value
                previous.next = Node(value)
                previous.next.next = current

            return None

        # Call the recursive insert_rec to insert a given value
        return self.insert_rec(current.next, current, value, position-1)

    def insert(self, value, position):
        """This is a method that will use a helper function to insert a given value into the
        linked list"""

        # Call the recursive function
        self.insert_rec(self.head, None, value, position)

    def reverse_rec(self, current):
        """This is a recursive helper function that will reverse the order of the linked list"""

        # If the list is empty, return None
        if current is None:
            return None

        # If the next Node value is none or at the end of the list, the current value is returned
        if current.next is None:
            self.head = current
            return current

        # Call the recursive reverse_rec function to return the current value and replace every value
        # until it is fully reversed
        else:
            temp = self.reverse_rec(current.next)
            temp.next = current
            current.next = None
            return current

    def reverse(self):
        """This is a method called reverse that will use a helper function to reverse the
        linked list"""

        # Call the helper recursive function
        self.reverse_rec(self.head)

    def is_empty(self):
        """This is method called is_empty and will determine if the linked list is empty"""

        # Return True if the list is empty and False if it is not
        return self.head is None
