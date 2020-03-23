# Author:      Jacob Hendry
# Date:        02/12/2020
# Description: This is a python file called row_puzzle.py. It will include a method called
#              row_puzzle that will take a list as a parameter to determine if the row is
#              solvable. A row is only solvable if a "token" can make it through the list
#              until it reaches the 0 at the end of the list.


def row_puzzle(some_list, pos=0):
    """This is a method called row_puzzle that will include a recursion call to determine
    if a row of integers will be solvable or not with a parameter as a list."""

    # The positive integer in the current position will be placed into a variable called num
    num = some_list[pos]

    # If the integer is -1, return False
    if num == -1:
        return False

    # If the integer is equal to zero, return True
    if num == 0:
        return True

    else:
        # Initialize the position to previous position
        some_list[pos] = -1

        # Initialize the movements to False
        go_left = go_right = False

        # If the addition of the position and the num in the position is larger than the list, continue
        if pos+num < len(some_list):

            # Recursively call the method to move the token left
            go_left = row_puzzle(some_list, pos+num)

        # If zero is less than or equal to the position minus the number, then move the token right
        if 0 <= pos-num:

            # Recursively call the method to move the token right
            go_right = row_puzzle(some_list, pos-num)

        # If either of the movements are true, return true
        if go_left == True or go_right == True:

            return True

        # Return false if the token can't move
        return False
