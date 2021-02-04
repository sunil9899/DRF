import requests

# URL = "http://127.0.0.1:8000/studata/3/"

# res = requests.get(url=URL)
# print(res.json())


URL = "http://127.0.0.1:8000/studataall/"

res = requests.get(url=URL)
print(res.json())
