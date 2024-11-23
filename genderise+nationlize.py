import requests
import json
# import library
name = input("whats your name : ").title()
# printing dictionary
Url =  f"https://api.nationalize.io/?name={name}"
name_response = requests.get(Url).text
name_dict = json.loads(name_response)
name1 = name_dict['name']
country = name_dict['country'][0]["country_id"]
# variables and json use
for key in name_dict:
    print (f"{key}: {name_dict[key]}")
print(f"{name1} {country}")
# print dictionary
Url =  f"https://api.agify.io/?name={name}"
age_response = requests.get(Url).text
age_dict = json.loads(age_response)
age1 = age_dict['name']
# variables and json use
for key in age_dict:
    if age_dict[key] is None:
        print("It is hard to guess your age")
    else:
         print (f"{key}: {age_dict[key]}")
# print dictionary























