# Author:      Jacob Hendry
# Date:        1/28/2020
# Description: This is a python file name file_sum.py. This file will have a function
#              named file_sum. The function will open a text file, add all the numbers
#              together, and return the sum.


def file_sum(filename):
    """This is a function named file_sum. It will take an existing file as a parameter,
    open the file, add the numbers up for a total, and then open a file named sum.txt
    that returns the total"""

    # Initialize the total to zero
    total = 0

    # Open the file 'filename' in read mode
    with open(filename, 'r') as inputs:

        # Loop through the file on every line
        for line in inputs:

            # Calculate the total
            total += float(line)

    # Open the file 'sum.txt' in write mode
    with open('sum.txt', 'w') as output:

        # Write the total number only
        output.write(str(total) + '\n')
