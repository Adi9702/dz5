
def dt (a, d):
    return a + d


# def minus (a, b):
#     return a - b



import requests

response = requests.get("https://httpbin.org/get")
print(response.json())