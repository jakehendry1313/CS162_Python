# Author:      Jacob Hendry
# Date:        1/8/2020
# Description: This is a python file named basic_stats.py. This file will compute
#              the mean, median, and mode of the ages of people from a class called
#              Person, which includes their name and age. The function basic_stats
#              will import the statistics module to find the mean, median and mode
#              to return it through the print function as a tuple.

import statistics
# This will import the statistics module


class Person:
    """This class will hold two data members - name and age"""

    def __init__(self, name, age):
        """This function will use an init method for two values
        to create initialized data members called name and age"""
        self.name = name
        self.age = age


def basic_stats(list_of_ages):
    """This function will use the imported statistics module to find
    the mean, median, and mode using the list of ages"""

    new_ages_list = []
    for Class_name in list_of_ages:
        new_ages_list.append(Class_name.age)

    mean = statistics.mean(new_ages_list)
    # The average_num variable will hold the value for the average of ages

    median = statistics.median(new_ages_list)
    # The middle_num variable will hold the middle number of all the ages

    mode = statistics.mode(new_ages_list)
    # The most_used variable will hold the most listed number of the ages list

    return mean, median, mode
    # Returns the mean, median, and mode to the print function
