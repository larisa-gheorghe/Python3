import requests
url = "https://icanhazdadjoke.com/"

# response = requests.get(url, headers={"Accept": "text/plain"})
# response = requests.get(url, headers={"Accept": "text/html"})
response = requests.get(url, headers={"Accept": "application/json"})

val1 = response.text
print(val1)
print(type(val1))       # <class 'str'>

val2 = response.json()
print(val2)
print(type(val2))       # <class 'dict'>
print(val2["joke"])