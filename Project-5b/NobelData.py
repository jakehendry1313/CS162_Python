# Author:      Jacob Hendry
# Date:        1/28/2020
# Description: This is a python file name NobelData.py. This file will have one class with an init
#              and search method. The class is named NobelData that will read a JSON file filled
#              with Nobel Prize winners. The search method will search for the given year and
#              category of Nobel Prize categories.

# Import the json module
import json


class NobelData:
    """This is a class called NobelData. It will have an init method that will open a json file
    named 'nobels.json' and reads the entire file. It will also have one method that searches
    the json file for nobel prize winners based on the given year and category"""

    def __init__(self):
        """This is an init method that will open and read a json file named nobel.json"""

        # Open the json file in read mode
        with open('nobels.json', 'r') as infile:

            # Read the json file into a python object
            self.winners_list = json.load(infile)

    def search_nobel(self, year, category):
        """This is a method called search_nobel that will search for nobel prize winners based
        on the given data members (year and category)"""

        # Initialize the length of prizes
        list_a = len(self.winners_list['prizes'])

        # Initialize a list for winners
        winners = []

        # Loop through the list of prizes
        for index in range(0, list_a):

            # If the year and category equal both of the indexes within the file, continue
            if self.winners_list['prizes'][index]['year'] == year and \
                    self.winners_list['prizes'][index]['category'] == category:

                # Add all of the laureates into the winners list
                winners = self.winners_list['prizes'][index]['laureates']
                break

        # Initialize the length of the winners
        list_b = len(winners)

        # Initialize a list of surnames of the winners
        surnames = []

        # Loop through the list of winners
        for i in range(0, list_b):

            # Add only the surnames of the winners to the list
            surnames.append(winners[i]['surname'])

        # Sort the surnames
        surnames.sort()

        # Return the surnames of the winners based on the year and category
        return surnames
