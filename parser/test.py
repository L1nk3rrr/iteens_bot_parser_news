import requests

r = requests.get("https://www.youtube.com/")

print(r.content)