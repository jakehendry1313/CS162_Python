# Author:      Jacob Hendry
# Date:        01/15/2020
# Description: This is a python file called Store.py. The file will contain three classes
#              named Product, Customer, and Store. The Product class will hold data members
#              to identify a product based on an ID code, title, description, price, and
#              quantity available. The Customer class will have data members to identify
#              a customer's name and ID code as well as creating a cart filled with products
#              and whether or not they are a premium member of the store. The Store class
#              will hold an inventory of products and a list of customers and being able to
#              checkout from the store as well.

import re
# Need to import the re module to use the search function

# Create a class called Product


class Product:
    """This class will hold five private data members - ID code, title, description, price, and quantity
    available and it will also have get methods for each data members as well as a decrease quantity method"""

    def __init__(self, id_code, title, description, price, quantity_available):
        """This init method will initialize the five data members that will be
        used to identify a product of the store"""

        self._id_code = id_code
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_id_code(self):
        """This is a get method that will return the id code of a product"""
        return self._id_code

    def get_title(self):
        """This a get method that will return the title of a product"""
        return self._title

    def get_description(self):
        """This is a get method that will return the description of a product"""
        return self._description

    def get_price(self):
        """This is a get method that will return the price of a product"""
        return self._price

    def get_quantity_available(self):
        """This is a get method that will return the quantity available of a product"""
        return self._quantity_available

    def decrease_quantity(self):
        """This function will decrease the quantity available by one"""
        self._quantity_available -= 1

# Create a class named Customer


class Customer:
    """This class called Customer will hold three data members - customer's name, customer's
    account ID, and whether or not they are a premium member of the store"""

    def __init__(self, name, account_ID, premium_member):
        """This init method will initialize the three data members that will be used
        to identify a customer of the store"""

        self._name = name
        self._account_ID = account_ID
        self._premium_member = premium_member
        self.cart = []
        # The cart data member will represent the Customer's cart to hold products

    def get_name(self):
        """This get method will be used to return the name of a customer"""
        return self._name

    def get_account_ID(self):
        """This get method will be used to return the account ID of a customer"""
        return self._account_ID

    def is_premium_member(self):
        """This function will return True if the customer is a premium member and false if not"""
        if self._premium_member:
            return True
        else:
            return False

    def add_product_to_cart(self, product_ID):
        """This function will add a product's ID code to the customer's cart"""
        self.cart.append(product_ID)

    def get_cart(self):
        return self.cart

    def empty_cart(self):
        """This function will empty the customer's cart"""
        self.cart.clear()


class InvalidCheckoutError(Exception):
    """This class will be an exception for when the customer tries to checkout
    and they are not a member"""
    pass

# Created the Store class here


class Store:
    """This class will have two data members that will hold the inventory of the store and
    customers of the store"""

    def __init__(self):
        """This init method will initialize two data members - inventory list and customers list"""

        self._inventory = []
        self._members_list = []

    def add_product(self, product):
        """This function will add a product to the stores inventory list"""
        self._inventory.append(product)

    def add_member(self, member):
        """This function will add a new member to the stores member list"""
        self._members_list.append(member)

    def get_product_from_ID(self, product_ID):
        """This function will return the name of the product with the matching id code
        and if it's not there it will return a special value called None"""

        for product in self._inventory:

            # This will determine if the given ID matches a product from the stores inventory list
            if product.get_id_code() == product_ID:

                # If the ID is found, then it returns the products ID and title
                return product.get_id_code()
            else:

                # If the ID code is not found, then it returns None
                return None

    def get_member_from_ID(self, member_ID):
        """This function will return the name of the member with the matching id code
        and if it's not there it will return a special value called None"""

        for member in self._members_list:

            # This will determine if the given ID matches a member from the stores member list
            if member.get_account_ID() == member_ID:

                # Returns the members account ID and the members name
                return member.get_account_ID
            else:

                # Returns None if no member is found
                return None

    def product_search(self, word):
        """This function will search for a product in the inventory list and will return a
        sorted list of ID codes based on a product being searched"""

        ID_search = []
        # Create a list to hold all of the ID's found

        for product in self._inventory:

            # Search the imported "word" in every product title and/or description
            if re.search(word, product.get_title(), re.IGNORECASE) or re.search(word, product.get_description(),
                                                                                re.IGNORECASE):
                # Add all of the ID codes to the newly created list
                ID_search.append(product.get_id_code())

        # Return a sorted list of ID codes found based on the imported "word"
        return sorted(ID_search)

    def add_product_to_member_cart(self, product_ID_code, member_account_ID):
        """This function will add a product to a members cart only if the product ID
        and member ID are found unless the product is out of stock"""

        for product in self._inventory:

            # Checks to see if the product ID matches the given product ID
            if product.get_id_code() == product_ID_code:
                product_search(product_ID_code)
                for member in self._members_list:

                    # Checks to see if the member ID matches the given member ID
                    if member.get_account_ID() == member_account_ID:

                        # Checks to see the product is available
                        if product.get_quantity_available() > 0:

                            # Adds the product to the member's cart if everything is True
                            member.add_product_to_cart(product)

                            # Returns the following statement
                            return "product added to cart"

                        else:
                            # Returns the following statement if the product is out of stock
                            return "product out of stock"
                    else:
                        # Returns the following statement if the member ID isn't found
                        return "member ID not found"

            else:
                # Returns the following statement if the product ID isn't found
                return "product ID not found"

    def check_out_member(self, member_ID):
        """This function will check a member out of the store if the product ID and member
        ID are found and then determines the charges whether the member is a premium member
        or not."""

        # Initiate the total charge to zero
        total_charge = 0.0



        for member in self._members_list:
            if member.get_account_ID() == member_ID:





                    product.decrease_quantity()
                    total_charge = total_charge + product.get_price()

                    # Determine the total charge based on all of the products prices
                    # Determines if the member is a premium member or not
                    if member.is_premium_member():

                        # If they are a premium member, shipping cost is $0
                        return total_charge

                    else:

                        # Returns the total charge for non premium members
                        return total_charge + (total_charge * 7 / 100)

            else:
                # This error will show up if the member ID doesn't exist
                raise InvalidCheckoutError

# Create a main function to run as a script


if __name__ == "__main__":

    try:
        product_1 = Product("123", "Doggy Treats", "The best treats for a best friend", 12.00, 10)
        customer_1 = Customer("Jacob", "ABC", False)
        my_store = Store()
        my_store.add_product(product_1)
        my_store.add_member(customer_1)
        print(my_store.add_product_to_member_cart("123", "ABC"))
        print(my_store.add_product_to_member_cart("123", "ABC"))
        print(my_store.check_out_member("ABC"))
    except InvalidCheckoutError:
        print("ERROR!! - You must be a member of the store to checkout.")