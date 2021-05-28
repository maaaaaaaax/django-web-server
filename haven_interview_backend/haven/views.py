from django.http import HttpResponse
import json
import requests

def index(request, propertyId):
    url_1 = "https://odrx4hmnq6.execute-api.us-west-2.amazonaws.com/default/interview_api_endpoint_1?propertyId=" + str(propertyId)
    url_2 = "https://ry1jrxwgeg.execute-api.us-west-2.amazonaws.com/default/interview_api_endpoint_2?propertyId=" + str(propertyId)
    r_1 = requests.get(url_1)
    r_2 = requests.get(url_2)
    # return HttpResponse("Hello, world. You're at the polls index.")
    data_1 = r_1.json()
    data_2 = r_2.json()
    result = {}
    if data_1["status"] == "success":
        print()
        print("API Endpoint 1: ")
        print(data_1)
        print()
        result["API Endpoint 1"] = data_1
    if data_2["status"] == "success":
        print()
        print("API Endpoint 2: " )
        print(data_2)
        print()
        result["API Endpoint 2"] = data_2
    if data_1["status"] != "success" and data_2["status"] != "success":
        result["status"] = "not_found"

    return HttpResponse(str(result))