import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE+"hello-world/charlie")
# print(response.json())
#
# print(requests.post(BASE+"hello-world/ankit").json())

print(requests.put(BASE + "video/1", {"likes": 10, "name": "test", "views": 10}).json())
print(requests.put(BASE + "video/1", {"likes": 10, "name": "test", "views": 10}).json())
print(requests.delete(BASE + "video/1"))
