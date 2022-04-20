import requests
import json
import jsonpath

#API URL
url = "http://127.0.0.1:5000/post_delete/1/"

response = requests.delete(url)

print(response.status_code)

assert response.status_code == 204
