import requests
import json
import jsonpath

def test_create_new_record():
    #API URL
    url = "http://127.0.0.1:5000/post"

    file = open('postBody.json','r')

    json_input = file.read()

    # Convert string to json
    request_json = json.loads(json_input)
    print("REQUEST",request_json)

    #Make post with json input
    respose = requests.post(url,request_json)
    print("RESPONSE",respose)

    print(respose.content)

    assert respose.status_code == 201
