# Author:      Jacob Hendry
# Date:        1/29/2020
# Description: This is a python file called box_sort. It will have one class called Box with a method
#              called volume. It will also have a function named box_sort as an insertion sort.


class Box:
    """This is a class named Box. It will contain the data members length,
    width, and height for a box."""

    def __init__(self, length, width, height):
        """This init method will initialize the data members length, width and height"""

        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        """This is a method named volume. It will return the volume of a box"""
        return self.length * self.width * self.height


def box_sort(some_list):
    """This is a insertion sort function that will take the list of Boxes, calculate the
    volume of each Box, and sort them from greatest to least"""

    # Go through the list of indexes of some_list
    for index in range(1, len(some_list)):

        # The variable a_box will identify a specific index in some_list
        a_box = some_list[index]

        # The variable position will help start the list at 0 and go up index - 1
        position = index - 1

        # While the position is true at 0 and above, the volume of a box is larger than the position's index continue
        while position >= 0 and a_box.volume() > some_list[position].volume():

            # If it is larger then switch the index's element position to one position ahead
            some_list[position + 1] = some_list[position]
            position -= 1

        # Now the current box is in a new position
        some_list[position + 1] = a_box
