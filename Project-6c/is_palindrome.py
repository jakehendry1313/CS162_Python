# Author:      Jacob Hendry
# Date:        02/12/2020
# Description: This is a python file named is_palindrome.py. It will include a method that will
#              take a string as parameter to determine if it is a palindrome. If it is, it will
#              return True, but if it isn't, it will return False.


def is_palindrome(str1):
    """This is a method called is_palindrome. It will take a string as a parameter to determine
    if the string is a palindrome"""

    # If the string is empty, return True
    if str1 == "":
        return True

    else:
        # If the first letter of the string is the same as the last letter, continue
        if str1[0] == str1[-1]:

            # Return a recursive call to the method to transverse through the string
            return is_palindrome(str1[1:-1])
        else:

            # Return False if the string is not a palindrome
            return False
