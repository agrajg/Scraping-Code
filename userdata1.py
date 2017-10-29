# importing packages
import urllib2
import requests
import csv
import json
import re

# obtaining input
# username_ex = "hannahhossack"

username_list = ["hannahhossack", "semaev", "desi37", "jennie1011",  "shas21cor", "sarahjenkinson7", "mandamandagirl"]
username_ex = "semaev"
token_ex = "AewmLJ9O3EgJJR_MfFZVJ-5ZgIh9FJ7vJqgiWzJDfVOF9MBAhQAAAAA"
url_ex = "https://api.pinterest.com/v1/users/hannahhossack/?access_token=&fields=first_name%2Cid%2Clast_name%2Curl%2Caccount_type%2Cusername%2Cbio%2Ccounts%2Ccreated_at%2Cimage"


# Search user function
def search_user(username, token):
    print ("==========================================================================================================")
    url = 'https://api.pinterest.com/v1/users/'+ username +'/?access_token=' + token +'&fields=first_name%2Cid%2Clast_name%2Curl%2Caccount_type%2Cbio%2Ccounts%2Ccreated_at%2Cimage%2Cusername'
    print "URL = " + url
    json_obj = urllib2.urlopen(url)
    print ("----------------------------------------------------------------------------------------------------------")
    data = json.load(json_obj)['data']
    obj_username = data['username']
    print obj_username
    # Regular expression
    rx = re.compile('[^a-zA-Z0-9_\'.!,]')
    obj_bio = rx.sub(' ', data['bio']).strip()
    print obj_bio
    obj_first_name = data['first_name']
    print obj_first_name
    obj_last_name = data['last_name']
    print obj_last_name
    obj_account_type = data['account_type']
    print obj_account_type
    obj_url = data['url']
    print obj_url
    obj_created_at = data['created_at']
    print obj_created_at
    obj_id = data['id']
    print obj_id
    print ("----------------------------------------------------------------------------------------------------------")
    counts_data = data['counts']
    obj_counts_pins = counts_data['pins']
    print obj_counts_pins
    obj_counts_following = counts_data['following']
    print obj_counts_following
    obj_counts_followers = counts_data['followers']
    print obj_counts_followers
    obj_counts_boards = counts_data['boards']
    print obj_counts_boards
    obj_counts_likes = counts_data['likes']
    print obj_counts_likes
    print ("----------------------------------------------------------------------------------------------------------")
    image_data = data['image']['60x60']
    obj_image_url = image_data['url']
    print obj_image_url
    obj_image_width = image_data['width']
    print obj_image_width
    obj_image_height = image_data['height']
    print obj_image_height
    print ("==========================================================================================================")
    writer.writerow({'username': obj_username, 'bio': obj_bio, 'first_name': obj_first_name, 'last_name': obj_last_name,
                     'account_type': obj_account_type, 'url': obj_url, 'created_at': obj_created_at, 'id': obj_id,
                     'count_pins': obj_counts_pins, 'count_following': obj_counts_following,
                     'count_followers': obj_counts_followers, 'count_boards': obj_counts_boards,
                     'count_likes': obj_counts_likes,
                     'image_url': obj_image_url, 'image_width': obj_image_width, 'image_height': obj_image_height})



with open('user_data_try1.csv', 'w') as csvfile:
    fieldnames = ['username', 'bio', 'first_name', 'last_name', 'account_type', 'url', 'created_at', 'id',
                  'count_pins', 'count_following', 'count_followers', 'count_boards', 'count_likes',
                  'image_url', 'image_width', 'image_height']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for uname in pin_list:
        # Calling search function
        search_user(uname, token_ex)
