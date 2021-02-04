import requests
import json

# URL = "http://127.0.0.1:8000/studetail/"


class StudentApp:
    def __init__(self):
        self.url = "http://127.0.0.1:8000/studetail/"

    def getData(self, id=None):
        data = {}
        if id is not None:
            data = {'id': id}
        json_data = json.dumps(data)
        res = requests.get(url=self.url, data=json_data)
        print(res.json())

    def createData(self):
        data = {
            'name': 'Amit',
            'roll': 103,
            'section': 'Out Smart'
        }
        json_data = json.dumps(data)
        res = requests.post(url=self.url, data=json_data)
        print(res.json())

    def updateData(self):
        data = {
            'id': 6,
            'roll': 70103758,
            'section': 'Dish TV'
        }
        json_data = json.dumps(data)
        res = requests.put(url=self.url, data=json_data)
        print(res.json())

    def deleteData(self):
        data = {'id': 5}
        json_data = json.dumps(data)
        res = requests.delete(url=self.url, data=json_data)
        print(res.json())


stu = StudentApp()
# stu.getData(2)
stu.createData()
# stu.updateData()
# stu.deleteData()
