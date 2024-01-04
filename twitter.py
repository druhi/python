import re

url = input("URL: ").strip()

username = re.sub(r"^https://druhi\.cf/", "", url)

print(f"Username: {username}")