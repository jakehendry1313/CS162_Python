# Author:      Jacob Hendry
# Date:        01/16/2020
# Description: This python file is called StoreTester.py. This file will import unittest to run at
#              least 5 unit tests and have at least 3 different assert functions.

import unittest
from Store import Store, Product, Customer, InvalidCheckoutError


class TestStore(unittest.TestCase):

    def test_1(self):

        product_1 = Product("201", "Red Jacket", "coats of all the coats", 21.99, 5)
        customer_1 = Customer("Jacob", "ABC", True)
        my_store = Store()
        my_store.add_product(product_1)
        my_store.add_member(customer_1)
        with self.assertRaises(InvalidCheckoutError):
            (my_store.check_out_member("DEF"))

    def test_2(self):
        product_1 = Product("123", "Doggy Treats", "The best treats ever", 12.99, 10)
        customer_1 = Customer("Jacob", "DEF", False)
        my_store = Store()
        my_store.add_product(product_1)
        my_store.add_member(customer_1)
        with self.assertRaises(InvalidCheckoutError):
            (my_store.check_out_member("ABC"))

    def test_3(self):
        product_1 = Product("123", "Doggy Treats", "The best treats ever", 12.99, 10)
        customer_1 = Customer("Jacob", "DEF", False)
        my_store = Store()
        my_store.add_product(product_1)
        my_store.add_member(customer_1)
        self.assertEqual(my_store.add_product_to_member_cart("123", "DEF"), "product added to cart")

    def test_4(self):
        product_1 = Product("201", "Red Jacket", "coats of all the coats", 21.99, 5)
        customer_1 = Customer("Jacob", "ABC", True)
        my_store = Store()
        my_store.add_product(product_1)
        my_store.add_member(customer_1)
        self.assertNotEqual(my_store.add_product_to_member_cart("201", "ABC"), "product out of stock")

    def test_5(self):
        product_1 = Product("201", "Red Jacket", "coats of all the coats", 21.99, 5)
        customer_1 = Customer("Jacob", "ABC", True)
        my_store = Store()
        my_store.add_product(product_1)
        my_store.add_member(customer_1)
        with self.assertRaises(InvalidCheckoutError):
            my_store.check_out_member("XYZ")


if __name__ == '__main__':

    unittest.main()
