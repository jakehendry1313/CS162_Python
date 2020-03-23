# Author:      Jacob Hendry
# Date:        1/28/2020
# Description: This is a python file name NeighborhoodPets.py. It will contain a class called
#              NeighborhoodPets that will have an add pet method, a delete pet method, get methods
#              for the owner of the pet and all of the species, saving and reading json files methods.


# import the json module
import json


class NeighborhoodPets:
    """This is a class named NeighborhoodPets. It will have a init method that will initiate the
    full list of pets. It will have multiple methods to add and delete pets, read and write
    json files, get the owner and full list of species"""

    def __init__(self):
        """This is an init method. It will initialize the the pet library/list"""

        # Initialize the list of pets into a dictionary
        self.list_of_pets = {}

    def add_pet(self, pet_name, species, owner):
        """This method is called add_pet and it will add a pet by the name, species, and
        the owner's name"""

        # if name isn't already in the list, then add the pet
        if pet_name not in self.list_of_pets.keys():

            # Add the pet by name, species and with owner's name
            self.list_of_pets[pet_name] = {"name": pet_name, "species": species, "owner": owner}

        # If the name is already in the list, then just return
        else:
            return

    def delete_pet(self, pet_name):
        """This method is called delete_pet. It will delete a pet by only the pet's name"""

        # If the name of the pet is in the list, then delete the pet
        if pet_name in self.list_of_pets.keys():

            # Pop out the name of the pet of the list
            self.list_of_pets.pop(pet_name)

    def get_owner(self, pet_name):
        """This method is called get_owner. It will return the name of the owner based
        on the pets name"""

        # If the pets name is in the list of pets, then return the name of the owner
        if pet_name in self.list_of_pets.keys():
            return self.list_of_pets[pet_name]["owner"]

        # If the pets name isn't in the list of pets, then just return
        else:
            return

    def save_as_json(self, filename):
        """THis is a method named save_as_json. It will save the list of pets onto the given
        filename of a json file"""

        # Initialize the list of pets into a python object
        some_data = self.list_of_pets

        # Open the json file into write mode
        with open(filename, 'w') as outfile:

            # Dump the all of the pets data into the json file
            json.dump(some_data, outfile)

    def read_json(self, filename):
        """This is a method called read_json. It will read a json file based on the given
        filename"""

        # Open the json file into read mode
        with open(filename, 'r') as infile:

            # Place all of the json file data into a python object
            self.list_of_pets = json.load(infile)

    def get_all_species(self):
        """This method is called get_all_species. It will return the list of all pets as
        a set"""

        # Put all of the species in the list of pets into a set called set_of_pets
        set_of_pets = {pet["species"] for pet in self.list_of_pets.values()}

        # Return the set
        return set_of_pets
