import requests
import json


URL = 'http://127.0.0.1:8000/'


def createData():
    data = {
        'name': 'Amit',
        'roll': 100,
        'section': 'PVT. Job',
        'city': 'Dubai',
    }
    json_data = json.dumps(data)
    res = requests.post(url=URL, data=json_data)
    print(res.json())


createData()
