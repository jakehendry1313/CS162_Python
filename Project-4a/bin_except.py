# Author:      Jacob Hendry
# Date:        1/28/2020
# Description: This is a python file name bin_except. It will have a binary search function
#              that will return an exception rather than -1.


class TargetNotFound(Exception):
    """This is an error exception that will be thrown if the target isn't found in the list"""
    pass


def bin_except(some_list, target):
    """This is a binary search function that will search for a given target"""

    begin = 0
    # Set the variable 'begin' to zero for the beginning of the list

    last = len(some_list) - 1
    # Set the variable 'last' to the length of the list minus one to get the end of the list

    while begin <= last:
        # Use a while loop to iterate through the list

        middle = begin + (last - begin) // 2
        # Find the middle index

        if some_list[middle] == target:
            return middle
        # If the middle index equals the target element return

        elif some_list[middle] < target:
            begin = middle + 1
        # Find the target above the middle index

        else:
            last = middle - 1
        # Find the target below the middle index

    raise TargetNotFound
    # Raise the exception if the target isn't found
