# Author:      Jacob Hendry
# Date:        02/11/2020
# Description: This is a python file called is_decreasing. It will have a method called
#              is_decreasing that will take a list as a parameter to determine if the list
#              is decreasing and will return True but if it's not it will return false.


def is_decreasing(a_list, pos=0):
    """This is a method called is_decreasing. It will take a list as a parameter to determine if
    the list is decreasing based on the values."""

    # If the length of the list is less than 2, return False
    if len(a_list) < 2:
        return False

    # If the current position is equal to the length of the list, return True
    if pos == len(a_list)-1:
        return True

    # If the current position is not equal to the length, continue
    else:

        # If the current position is greater than the next position, continue
        if a_list[pos] > a_list[pos+1]:

            # Calls a method recursively with a new current position
            return is_decreasing(a_list, pos+1)

        # If the current position is less than the next position, return False
        else:
            return False
