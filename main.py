# def main():
#     print("Hello from venv!")


# if __name__ == "__main__":
#     main()



# import os, sys, datetime, json 
# print(os.getcwd())

# import math_utils
# print(math_utils.add(5, 5))

# from math_utils import add
# print(add(5, 5))

# from math_utils import *
# print(minus(10, 5))

import requests

response = requests.get("https://httpbin.org/get")
print(response.json())