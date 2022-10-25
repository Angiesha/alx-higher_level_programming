#!/usr/bin/python3
"""Takes in a string and sends a search request to the Star Wars API"""

if __name__ == "__main__":
    import requests
    import sys

    r = requests.get('https://swapi.co/api/people/?search={}'
                     .format(sys.argv[1])).json()
    print('Number of results: {}'.format(r.get('count')))
    for res in r.get('results'):
        print(res.get('name'))
