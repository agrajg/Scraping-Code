# importing packages
import urllib2
imprort
import requests
import csv
import json

# obtaining input
username_ex = "hannahhossack"
token_ex = "AewmLJ9O3EgJJR_MfFZVJ-5ZgIh9FJ7vJqgiWzJDfVOF9MBAhQAAAAA"
url_ex = "https://api.pinterest.com/v1/users/hannahhossack/?access_token=&fields=first_name%2Cid%2Clast_name%2Curl%2Caccount_type%2Cusername%2Cbio%2Ccounts%2Ccreated_at%2Cimage"

# Search user function
def search_user(username, token):
    url = 'https://api.pinterest.com/v1/users/'+ username +'/?access_token=' + api_key +'&fields=first_name%2Cid%2Clast_name%2Curl%2Caccount_type%2Cbio%2Ccounts%2Ccreated_at%2Cimage%2Cusername'
    json_obj = urllib.request.urlopen(url)
    data = json.load(json_obj)
    print("URL")
    print(url)
    print("DATA")
    print(data)

# Calling search function
search_user(username_ex, token_ex)