#!/usr/bin/python3
"""Takes in a string and sends a search request to the Star Wars API"""

if __name__ == "__main__":
    import requests
    import sys

    with requests.Session() as s:
        r = s.get('https://swapi.co/api/people/?search={}'
                  .format(sys.argv[1])).json()
        print('Number of results: {}'.format(r.get('count')))
        while True:
            res = r.get('results')
            for re in res:
                print(re.get('name'))
                films = re.get('films')
                for film in films:
                    f = s.get(film).json()
                    print('\t{}'.format(f.get('title')))
            if r.get('next') is None:
                break
            else:
                r = s.get(r.get('next')).json()
