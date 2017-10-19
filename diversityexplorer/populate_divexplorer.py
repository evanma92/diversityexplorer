import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diversityexplorer.settings')

import django
django.setup()
from divexplorer.models import User, Simulation, Parameter

def populate():
    """
    Create lists of dictionaries containing the simulations we want to add for each
    user.
    Then we will create a dictionary of dictionaries for our users.
    This allows us to iterate through each data structure and add the data to our models.
    :return:
    """

    simulations = [
        {
            "email":"evanma92@gmail.com",
            "username":"evanma",
            "password":"scrabble"
        },
        {
            "email": "evan.asavaaree@u.yale-nus.edu.sg",
            "username": "evanma92",
            "password": "scrabble1"
        },
        {
            "email": "evanasavaaree@gmail.com",
            "username": "evanma1992",
            "password": "scrabble1234"
        }
    ]