import unittest
from flask.testing import client
from website.models import home, account



def test_account(unittest.TasteCase):
    response = client.get(reversed('salary'))
    assertEqual(response.status_code,312)



def test_home(unittest.TasteCase):
    response = client.get(reversed('home'))
    assertEqual(response.status_code,302)
    
