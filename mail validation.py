import re

email = input("whats your mail?").strip()

if re.search(r"^\w.+@(\w+\.\w+\.)?\w+\.(com|edu|in)$",email):
    print("valid")
else:
    print("invald")