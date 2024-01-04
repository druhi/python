import requests
import json

name = input("what is your name : ")
Url =  f"https://api.nationalize.io/?name={name}"

name_response = requests.get(Url).text
name_dict = json.loads(name_response)
name1 = name_dict['name']
country = name_dict['country'][0]["country_id"]

print(name1)
print(country)





