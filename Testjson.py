import json

with open('Progettofintech/NASDAQ.json') as json_file:
    data = json.load(json_file)
    for p in data:
        print('Name: ' + p['Company Name'])
        print('Codice: ' + p['Symbol'])