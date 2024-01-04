import requests
import json
name = input("whats your name : ").title()
url =f"https://api.genderize.io/?name={name}"
gender_response = requests.get(url).text
gender_dict = json.loads(gender_response)

gender1 = gender_dict['name']
country = gender_dict['gender']
# print(name)
# print(country)
# for i in gender_dict:
#     print(i)
for key in gender_dict:
    print (f"{key}: {gender_dict[key]}")


