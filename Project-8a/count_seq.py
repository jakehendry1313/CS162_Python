# Author:      Jacob Hendry
# Date:        02/25/2020
# Description: This is a python file called count_seq.py. It will contain a generator function
#              that will count how many of each number in a row in a previous number and will be
#              infinite.


def count_seq():
    """This is generator function that will count each number in a row in the previous number"""

    # Start the sequence with the number 2
    num = '2'

    # Loop the sequence infinitely
    while True:

        # Yield each num that is return after each loop
        yield int(num)

        # Create an empty string
        next_num = ''

        # Loop through the sequence until each number has been read
        while len(num) > 0:

            # Initialize the first number as a data member called current
            current = num[0]

            # Start the count of the sequence at zero
            count = 0

            # Loop through the sequence until all numbers have been read
            while len(num) > 0 and num[0] == current:

                # Increment count for the number
                count += 1

                # Remove the first number and iterate
                num = num[1:]

            # The next number is add as the count of the current number
            next_num += '{}{}'.format(count, current)

        # Now the next number is the full add numbers
        num = next_num
