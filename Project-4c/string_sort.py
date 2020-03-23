# Author:      Jacob Hendry
# Date:        01/29/2020
# Description: This is a python file named string_sort. This file will sort a list of
#              strings instead of numbers whiling ignoring the case of the strings.


def string_sort(some_list):
    """This is an insertion function that will sort strings of a list and ignore
    the case of the strings"""

    # Transverse through the inputted list
    for index in range(1, len(some_list)):

        # The variable temp will hold a specific index of the list
        temp = some_list[index]

        # pos will hold the position of the index
        pos = index - 1

        # If the position in the list is above 0 and the position left of the index is larger than the index
        while pos >= 0 and some_list[pos].lower() > temp.lower():
            # Use the .lower() method to lower all of the letters of the string to lower case

            # Replace the current position to the right
            some_list[pos + 1] = some_list[pos]

            # Move to the next position
            pos -= 1
        # The index is now in the next position
        some_list[pos + 1] = temp

    # Return the now sorted list
    return some_list
