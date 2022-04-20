import requests
import json
import jsonpath

#API URL
url = "http://127.0.0.1:5000/get"

#Fetching the response
response = requests.get(url)

#Print Response
print(response.content)

#Print Content Header
print(response.headers)

#Parse in json format
json_response = json.loads(response.text)

print(json_response)

name = jsonpath.jsonpath(json_response,'name')
print("NAME",name)