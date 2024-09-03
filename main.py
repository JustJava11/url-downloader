import requests

url = "https://http.cat/images/205.jpg"

with open("cat.jpg","wb")as f:
    f.write(requests.get(url).content)