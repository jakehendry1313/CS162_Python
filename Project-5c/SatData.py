# Author:      Jacob Hendry
# Date:        1/28/2020
# Description: This is a python file name SatData.py. It will include a class named SatData that will
#              read and write a SAT Data json file into a text file in csv (comma-separated values)
#              format. The class will have an init method that will open and read the json file and a method
#              called save_as_csv that will save the DBNs (district bureau numbers) of the New York schools.

# import the module json
import json


class SatData:
    """This is a class called SatData. It will have two methods called init and save_as_csv
    to read a json file, write to a text file in a csv format of the searched dbns"""

    def __init__(self):
        """This is an init method that will read a json file and read it into a python object"""

        # Open the json file in read mode
        with open('sat.json', 'r') as infile:

            # Read the json file into a python object
            self.data = json.load(infile)

            # Add all of the data section of the json file to a python object
            self.School = self.data['data']

            # Add all of the intro section of the json file to a python object
            self.Column = self.data['meta']['view']['columns']

    def save_as_csv(self, DBNs):
        """This is a method called save_as_csv that will open a csv file. It will search for the
        searched DBNs from the json file into a csv file."""

        # Open the csv file in write mode
        with open('output.csv', 'w') as outfile:

            # Loop through the names of the columns from the 8th index and up
            for i in self.Column[8:]:

                # Write the names into the csv file
                titles = i['name'] + ','

                # If the title name is the last name then remove the comma
                if i['name'] == self.Column[13]['name']:
                    titles = i['name']

                # Write the title names onto the csv file
                outfile.write(titles)

            # Make a new line after writing all of the names of the columns
            outfile.write('\n')

            # Loop through the data section of the json file
            for i in self.School:

                # If the dbns are in the searched DBNs, then continue
                if i[8] in DBNs:

                    # Add a comma after each element and add a new line after each searched DBN
                    dbns_list = ','.join([str(elem) for elem in i[8:]]) + "\n"

                    # Sort the dbns_list
                    sorted(dbns_list)

                    # Write the sorted dbns_list onto the csv file
                    outfile.write(dbns_list)
