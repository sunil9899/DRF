import requests
import json

URL = 'http://127.0.0.1:8000/'
data = {
    'name': 'Vikas',
    'age': 27,
    'roll': 23,
    'section': 'Intermediate'
}
json_data = json.dumps(data)
response = requests.post(url=URL, data=json_data)
print(response.json())
