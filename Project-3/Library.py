# Author:      Jacob Hendry
# Date:        01/22/2020
# Description: This is a python file called Library. It will have three classes called
#              LibraryItem, Patron, and Library. The LibraryItem class will have three subclasses that
#              inherit its data members and functions and they are called Book, Movie, and Album. The
#              Patron class will contain all the data members and functions to identify a patron of the
#              library. Lastly, the Library class will contain all the data members and functions to
#              hold Patron and LibraryItem information to check out, request items, return items and
#              pay Patron's fines.


class LibraryItem:
    """The LibraryItem class will contain data members (id_code and title) that are initialized
    to identify a Library item. It will also contain data members for the location, whether its
    checked out, who its requested by and the date it was checked out (number of days have past)."""

    def __init__(self, id_code, title):
        """This init method will help identify a book, movie, or album based on an id code,
        title, where its located, who it's checkout by or requested by and what date it was
        checked out."""

        self._id_code = id_code
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None             # Initialize the checked out by to None
        self._requested_by = None               # Initialize requested by to None
        self._date_checked_out = 0              # Initialize date checked out to 0 for the start of check out day

    def get_id_code(self):
        """This is a get method that will return the id code of a Library item"""
        return self._id_code

    def get_title(self):
        """This is a get method to return the title of an item in the Library"""
        return self._title

    def get_location(self):
        """This get method will return the location of an item"""
        return self._location

    def set_location(self, location):
        """This set method will set the location of an item"""
        self._location = location

    def get_checked_out_by(self):
        """This get method will return who checked out the item"""
        return self._checked_out_by

    def set_checked_out_by(self, checked_by):
        """This set method will set who checked out the item"""
        self._checked_out_by = checked_by

    def get_requested_by(self):
        """This get method will return who requested an item"""
        return self._requested_by

    def set_requested_by(self, request_by):
        """This set method will set who requested an item"""
        self._requested_by = request_by

    def get_date_checked_out(self):
        """This get method will return the date it was checked out"""
        return self._date_checked_out

    def set_date_checked_out(self, checkout_date):
        """This set method will set the date it was checked out"""
        self._date_checked_out = checkout_date


class Book(LibraryItem):
    """This is a subclass called Book. It inherits the LibraryItem's data members and functions.
    It will contain the id code and title from LibraryItem and as well as a data member called
    author."""

    def __init__(self, id_code, title, author):
        """This init method will initialize the inherited data members and the data member author"""
        super().__init__(id_code, title)    # Inherited the id_code and title data members from LibraryItem
        self._author = author

    def get_author(self):
        """This get method will return the name of the author of the book"""
        return self._author

    @staticmethod
    def get_check_out_length():
        """This get method is a static method that will return what the length for checkout is for
        a book"""
        return 21               # 21 Days for check out length; any days over will be overdue


class Album(LibraryItem):
    """This is a subclass called Album. It inherits the LibraryItem's methods and data members.
    It will also have a data member called artist."""

    def __init__(self, id_code, title, artist):
        """This init method will initialize the id code and title from the LibraryItem and the
        data member called author"""
        super().__init__(id_code, title)    # Inherited the id_code and title data members from LibraryItem
        self._artist = artist

    def get_artist(self):
        """This get method will return the name of the artist of the album"""
        return self._artist

    @staticmethod
    def get_check_out_length():
        """This get method is a static method that will return what the checkout length is for
        an album"""
        return 14               # 14 days for the checkout length; any days over is overdue


class Movie(LibraryItem):
    """This is a subclass called Movie. It inherits the data members and methods of LibraryItem.
    It also has a data member called director."""

    def __init__(self, id_code, title, director):
        """This init method will initialize the id code and title of LibraryItem as well as the
        data member called director"""
        super().__init__(id_code, title)    # Inherited the id_code and title data members from LibraryItem
        self._director = director

    def get_director(self):
        """This get method will return the name of the director"""
        return self._director

    @staticmethod
    def get_check_out_length():
        """This get method is a static method that will return the length of a checkout for a movie"""
        return 7                # 7 days for length of checkout; any days over will be overdue


class Patron:
    """This is class called Patron. It will hold data members (id_num and name) to identify
    a Patron of the Library. It will also have data members for checked out items and a fine
    amount based on if the the checked out item is overdue."""

    def __init__(self, id_num, name):
        """This init method will initialize the id number and name of the Patron"""
        self._id_num = id_num
        self._name = name
        self._checked_out_items = []        # Create a list for the items that are checked out
        self._fine_amount = 0               # Initialize the fine amount to zero

    def get_id_num(self):
        """This get method will return the id number of a Patron"""
        return self._id_num

    def get_name(self):
        """This get method will return the name of a Patron"""
        return self._name

    def get_fine_amount(self):
        """This get method returns the fine amount of the given Patron"""
        return self._fine_amount

    def add_library_item(self, library_item):
        """This function will add a library item to the Patron's checked out list"""
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """This function will remove an item from the Patron's checked out list"""
        self._checked_out_items.remove(library_item)

    def amend_fine(self, new_fines):
        """THis function will add the new fines to the current fine amount"""
        if new_fines > 0:
            self._fine_amount = self._fine_amount + new_fines
        else:
            self._fine_amount = new_fines - self._fine_amount

    def get_checked_out_items(self):
        """This function will return the Patron's checked out items"""
        return self._checked_out_items


class Library:
    """This is a class called Library. This class will contain the functions to add patron's and items,
    check out, request, and return items. It will also have a function to pay a Patron's fine amount."""

    def __init__(self):
        """This init function will contain the holdings and members dictionaries and initialize the current
        date to zero"""
        self._holdings = {}             # Dictionary for the Library holdings
        self._members = {}              # Dictionary for the Library members
        self._current_date = 0          # Initialize the current date to 0 to start check out day

    def add_library_item(self, lib_item):
        """This function will add a library item to the Library's holdings list"""
        self._holdings[lib_item.get_id_code()] = lib_item

    def add_patron(self, patron):
        """This function will add a patron to the Library's members list"""
        self._members[patron.get_id_num()] = patron

    def get_library_item(self, library_ID):
        """This get method will return the library item based on the items id if in the Library holdings"""
        if library_ID in self._holdings:
            return self._holdings[library_ID]
        else:
            return None

    def get_patron(self, pat_ID):
        """This get function will return the members name based on the members id if in the Library holdings"""
        if pat_ID in self._members:
            return self._members[pat_ID]
        else:
            return None

    def request_library_item(self, patron_ID, item_ID):
        """This function will request an item from the library by a patron and put the
        item on to the hold shelf"""

        patron = self.get_patron(patron_ID)         # Get the patron's id
        item = self.get_library_item(item_ID)       # Get the library item's id

        if patron is not None:
            if item is not None:

                # Determine if the library item is already requested
                if self._holdings[item_ID].get_location() != "ON_HOLD_SHELF":

                    # Set patron's id to requested by
                    self._holdings[item_ID].set_requested_by(patron_ID)

                    # Set location to on hold shelf
                    self._holdings[item_ID].set_location("ON_HOLD_SHELF")

                    return "request successful"

                else:
                    return "item on hold by other patron"
            else:
                return "item not found"
        else:
            return "patron not found"

    def check_out_library_item(self, patron_ID, lib_ID):
        """This function will check out a patron from the library with the given patron id and item id"""

        patron = self.get_patron(patron_ID)             # Return the patron's id
        item = self.get_library_item(lib_ID)            # Return the library item's id

        if patron is not None:
            if item is not None:

                # If the location of the item is not checked out, continue to the next if statement
                if self._holdings[lib_ID].get_location() != "CHECKED_OUT":

                    # If the item was not requested yet, continue to the next statement
                    if self._holdings[lib_ID].get_requested_by() != patron:

                        # Set the patron's Id to checked out by patron Id
                        self._holdings[lib_ID].set_checked_out_by(patron_ID)

                        # Set the current date to be the date checked out (should be 0)
                        self._holdings[lib_ID].set_date_checked_out(self._current_date)

                        # Set the new location to checked out for the library item
                        self._holdings[lib_ID].set_location("CHECKED_OUT")

                        # Set the new requested by to None
                        self._holdings[lib_ID].set_requested_by(None)

                        # Now add the library item to the patron's checked out items
                        self._members[patron_ID].add_library_item(lib_ID)

                        return "check out successful"
                    else:
                        return "item on hold by other patron"
                else:
                    return "item already checked out"
            else:
                return "item not found"
        else:
            return "patron not found"

    def return_library_item(self, item_ID):
        """This function will return a library item to the library based on the items id and
        return it to the shelf"""

        # Get the library item's id
        item = self.get_library_item(item_ID)

        if item is not None:

            # If the library item is checked out or on hold shelf, continue to the next statement
            if self._holdings[item_ID].get_location() == "CHECKED_OUT" or "ON_HOLD_SHELF":

                # Get whomever checked the library item out
                member = self._holdings[item_ID].get_checked_out_by()

                # Set the returned patron id to mem
                mem = self.get_patron(member)

                # Return the checked out items into a new list
                new_list = mem.get_checked_out_items()

                # Now search through the new list to find the item id
                for item_ID in new_list:
                    if item_ID in self._holdings:

                        # Now remove that item from the members checked out items list
                        mem.remove_library_item(item_ID)
                        return "return successful"

                    # If no one requested the item, return to the shelf and set requested by to None
                    if self._holdings[item_ID].get_requested_by is None:
                        self._holdings[item_ID].set_location("ON_SHELF")
                        self._holdings[item_ID].set_checked_out_by(None)
                    else:
                        # If some one did request it return to the hold shelf
                        self._holdings[item_ID].set_location("ON_HOLD_SHELF")
            else:
                return "item already in library"
        else:
            return "item not found"

    def pay_fine(self, patron_ID, amount_paid):
        """This function will pay the Patron's fine based on how many days its past due"""

        # Search the patron id in the members dictionary
        if patron_ID in self._members:

            # Now amend the amount paid to the fines
            self._members[patron_ID].amend_fine(amount_paid)
            return "payment successful"
        else:
            return "patron not found"

    def increment_current_date(self):
        """This function will increase the current date and add a fine if it's past due by 10 cents"""
        self._current_date += 1

        for item in self._holdings:
            # Check to see if the patron has checked out
            if self._holdings[item].get_checked_out_by() is not None:

                # Check to see if the current date minus the check out date is greater than the items checkout length
                if self._current_date - item.get_date_checked_out() > item.get_check_out_length():

                    # If it is then add 0.10 * the incremented date
                    item.amend_fine(0.1 * self._current_date)
                else:
                    return None
            else:
                return None
