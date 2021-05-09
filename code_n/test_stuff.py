import unittest 
from routes.views import home, stuff

def test_stuff(unittest.TasteCase):
    response = clint.get(reversed('stuff'))
    assertEqual(response.status_code,100)

def test_home(unittest.Tastease):
    response = clint.get(reversed('home'))
    assertEqual(response.status_code,200)   
