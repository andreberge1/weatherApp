import requests
import pandas as pd

client_id = "76aa5f7a-a2e6-4570-9815-00c64da19353"

endpoint = "https://frost.met.no/observations/v0.jsonld"
parameters = {
    "sources": "SN18700,SN90450",
    "elements": "mean(air_temperature P1D)",
    "referencetime": "2010-04-01/2010-04-03"
}

r = requests.get(endpoint, parameters, auth=(client_id, ""))
json = r.json()

if r.status_code == 200:
    data = json["data"]
    print("Data recieved")

else:
    print("Error:     " & r.status_code)