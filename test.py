import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE+"hello-world/charlie")
print(response.json())

print(requests.post(BASE+"hello-world/ankit").json())
