# Author:      Jacob Hendry
# Date:        02/25/2020
# Description: This is a python file called sort_timer.py. It will determine the amount of time
#              it takes to complete a bubble sort function versus a insertion sort function. It
#              will return a graph to show the difference.

import time
import random
from matplotlib import pyplot


def sort_time(func):
    """This is a decorator function that will return the amount of the time it takes to
    complete the sort functions"""

    def wrapper(*args):
        """This is the inner "wrapper" function that will return how long it takes to complete"""

        # Start time of the execution
        start = time.perf_counter()

        # Call the function
        func(*args)

        # Time after the execution
        end = time.perf_counter()

        # Return the amount of time it took to complete
        return end - start

    # Return the inner function
    return wrapper


def compare_sorts(func_1, func_2):
    """This function will compare a bubble sort and an insertion sort and will return a graph to represent
    the difference in time. It will take two decorated functions as parameters."""

    # Initialize two list for the times of each sort function
    bubble_list = []
    insert_list = []

    # Create a list of of the tested values
    test_values = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 100000]

    # Loop through the list to create the first list
    for k in test_values:
        list_1 = []

        # Find random numbers to sort
        for i in range(1, k+1):
            list_1.append(random.randint(1, 10000))

        # Create a second list the same as the first.
        list_2 = list(list_1)

        bubble_list.append(func_1(list_1))
        insert_list.append(func_2(list_2))

    # Graph both of the sort function
    pyplot.plot(test_values, bubble_list, 'ro--', lineWidth=2)
    pyplot.plot(test_values, insert_list, 'go--', lineWidth=2)
    pyplot.show()


# Wrap the sort time function on bubble sort function
@sort_time
def bubble_sort(a_list):
    """Sorts some list in ascending order"""

    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


# Wrap the sort time function on insertion sort function
@sort_time
def insertion_sort(a_list):
    """This will sort a list in ascending order"""

    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


compare_sorts(bubble_sort, insertion_sort)
