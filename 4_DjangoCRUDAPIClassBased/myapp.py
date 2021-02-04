import requests
import json

URL = "http://127.0.0.1:8000/"


def readData(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    res = requests.get(url=URL, data=json_data)
    print(res.json())


# readData(2)

def createData():
    data = {
        'name': 'Ajay Kabira',
        'roll': 344,
        'section': 'Business',
        'age': 37
    }
    json_data = json.dumps(data)
    res = requests.post(url=URL, data=json_data)
    print(res.json())


# createData()

def partialUpdate():
    data = {
        'id': 3,
        'name': 'Kamal Kumar',
        'age': 40
    }
    json_data = json.dumps(data)
    res = requests.put(url=URL, data=json_data)
    print(res.json())


# partialUpdate()

def deleteData(id):
    data = {'id': id}
    json_data = json.dumps(data)
    res = requests.delete(url=URL, data=json_data)
    print(res.json())


deleteData(2)
