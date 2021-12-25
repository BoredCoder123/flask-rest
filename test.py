import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE+"hello-world/charlie")
# print(response.json())
#
# print(requests.post(BASE+"hello-world/ankit").json())

# print(requests.put(BASE + "video/3", {"likes": 10, "name": "test", "views": 10}).json())
# print(requests.put(BASE + "video/4", {"likes": 10, "name": "test2", "views": 10}).json())
# print(requests.get(BASE + "video/6").json())
# print(requests.delete(BASE + "video/1"))
print(requests.patch(BASE+"video/1", {"views": 99}).json())
print(requests.get(BASE+"video/1").json())
print(requests.delete(BASE+"video/1"))
print(requests.get(BASE+"video/1").json)