# Author:      Jacob Hendry
# Date:        02/11/2020
# Description: This is a python file called array_max.py. It will include one recursive function
#              called array_max that will take a list as a parameter and returns the maximum value.


def array_max(a_list):
    """This is a method called array_max. It will take a list as a parameter and find the max of the list"""

    # If the list has only one element, return that element as the max number
    if len(a_list) == 1:

        # Return the first index
        return a_list[0]

    else:
        # Recursively call the function array_max to go through the list
        max_num = array_max(a_list[1:])

        # Return the max number if it's greater than the current index
        return max_num if max_num > a_list[0] else a_list[0]
