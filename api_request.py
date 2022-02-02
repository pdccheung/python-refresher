import requests

base_url = "https://swapi.dev/api/"

api_endpoint= "films/3"

req = requests.get(base_url+api_endpoint)
req_obj = req.json()

print(req_obj["title"])
