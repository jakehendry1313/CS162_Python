# Author:      Jacob Hendry
# Date:        01/29/2020
# Description: This is a python file called sorts_count. It will include two different functions -
#              bubble_count(bubble sort) and insertion_count(insertion sort) to find the number of
#              comparisons and exchanges within the sort functions


def bubble_count(some_list):
    """This is a bubble sort function that will count the number of exchanges and
    # comparisons that are made before returning a tuple of the two"""

    # Set the starting exchanges and comparisons equal to zero
    exchanges = 0
    comparisons = 0

    # Transverse through the list
    for num in range(len(some_list)):

        # Start at the beginning of the list
        for index in range(len(some_list) - num - 1):

            # Start adding comparisons
            comparisons += 1

            # If the first index is larger than the index to the right, then swap
            if some_list[index] > some_list[index + 1]:

                # Swap the indexes
                temp = some_list[index]
                some_list[index] = some_list[index + 1]
                some_list[index + 1] = temp

                # Add an exchange count
                exchanges += 1

    # Return the comparisons and exchanges as a tuple
    return comparisons, exchanges


def insertion_count(some_list):
    """This is an insertion function that will sort a list and return the number of
    # comparisons and exchanges it takes to sort the list"""

    # Start the exchanges and comparisons equal to zero
    exchanges = 0
    comparisons = 0

    # Transverse through the list
    for index in range(len(some_list)):

        # The variable key will hold a specific index
        key = some_list[index]

        # The variable pos will hold the position of the list
        pos = index - 1

        # If the position of the list starts at 0 and goes up with the while loop
        while pos >= 0:

            # Add comparisons by one
            comparisons += 1

            # If the key (current index) is larger than the index to the left
            if key < some_list[pos]:

                # Add exchanges by one
                exchanges += 1

                # Swap the position from left to right
                some_list[pos + 1] = some_list[pos]

                # Go to the next position
                pos -= 1
            else:
                break
        # The current index is placed in the next position
        some_list[pos + 1] = key

    # Return the comparisons and exchanges in a tuple
    return comparisons, exchanges
