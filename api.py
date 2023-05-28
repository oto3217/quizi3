import requests
import json
api_key = 'RGAPI-8b53a7ee-9897-4af1-a7a4-193b6bb38ae6'
api_url = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/UodbALAyc4z1KxmEPFpdCy1-lm-C90evN9mwqDVYd4CqtAmRlVw8Q_bJAOlEdjcqYrQCF5Xxar0_dQ/ids?start=0&count=20'
response = requests.get(api_url)
json_data = response.json()
filename = 'jsonformat.json'
matches = response.json()
with open(filename, 'w') as file:
    json.dump(json_data, file, indent=4)




print(response)
print(response.status_code)
print(response.headers)
print(response.text)
print(matches)