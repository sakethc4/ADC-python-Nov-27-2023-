import requests
import json 

Class CatFacts:
    def __init__(self): 
        self.api = 'https://catfact.ninja/breeds'

    def get_nth_cat_breed(self, n):
    # do get request
    results = requests.get(self.api)
    data = results.json()

    return data['data'][n-1]
