# external api calls in python
import requests
import json
import os

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
data = response.json()
print(data["title"])

founder_data = {
    "product" : "DistroAI",
    "audience" : "indie founders",
    "channels" : ["reddit","instagram","threads"]
    }

with open("founder.json", "w") as f:
    json.dump(founder_data,f,indent= 2)

with open("founder.json","r") as f:
    loaded = json.load(f)
    print(loaded["channels"])

os.environ["MY_KEY"] = "test123"
key = os.environ.get("MY_KEY", "not found")
print(key)