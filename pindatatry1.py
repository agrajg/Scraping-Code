# importing packages
import urllib2
import requests
import csv
import json
import re

# obtaining input
# username_ex = "hannahhossack"

pin_list = ["322500023298512556", "368169338263694786", "123075002296407594", "572097958893849460",  "561683384762501854", "205195326749941445", "578642252092590219"]
pin_ex = "368169338263694786"
token_ex = "AewmLJ9O3EgJJR_MfFZVJ-5ZgIh9FJ7vJqgiWzJDfVOF9MBAhQAAAAA"
url_ex = "https://api.pinterest.com/v1/pins/322500023298512556/?access_token=AewmLJ9O3EgJJR_MfFZVJ-5ZgIh9FJ7vJqgiWzJDfVOF9MBAhQAAAAA&fields=id%2Clink%2Cnote%2Curl%2Cattribution%2Cboard%2Ccolor%2Ccounts%2Ccreated_at%2Ccreator%2Cimage%2Cmedia%2Cmetadata%2Coriginal_link"
# Search user function
def search_user(pin, token):
    print ("==========================================================================================================")
    url = 'https://api.pinterest.com/v1/pins/'+ pin +'/?access_token=' + token +'&fields=id%2Clink%2Cnote%2Curl%2Cattribution%2Cboard%2Ccolor%2Ccounts%2Ccreated_at%2Ccreator%2Cimage%2Cmedia%2Cmetadata%2Coriginal_link'
    print "URL = " + url
    json_obj = urllib2.urlopen(url)
    print ("----------------------------------------------------------------------------------------------------------")
    data = json.load(json_obj)['data']
    obj_attribution = data['attribution']
    print obj_attribution
    obj_creator = data['creator']
    obj_creator_url = obj_creator['url']
    print obj_creator_url
    obj_creator_first_name = obj_creator['first_name']
    print obj_creator_first_name
    obj_creator_last_name = obj_creator['last_name']
    print obj_creator_last_name
    obj_creator_id = obj_creator['id']
    print obj_creator_id
    obj_url = data['url']
    print obj_url
    obj_media = data['media']
    obj_media_type = obj_media['type']
    print obj_media_type
    obj_created_at = data['created_at']
    print obj_created_at
    obj_original_link = data['original_link']
    print obj_original_link
    obj_note = data['note']
    print obj_note
    obj_color = data['color']
    print obj_color
    obj_link = data['link']
    print obj_link
    obj_board = data['board']
    obj_board_url = obj_board['url']
    print obj_board_url
    obj_board_id = obj_board['id']
    print obj_board_id
    obj_board_name = obj_board['name']
    print obj_board_name
    obj_image = data['image']
    obj_image_original = obj_image['original']
    obj_image_original_url = obj_image_original['url']
    print obj_image_original_url
    obj_image_original_width = obj_image_original['width']
    print obj_image_original_width
    obj_image_original_height = obj_image_original['height']
    print obj_image_original_height
    obj_counts = data['counts']
    obj_counts_likes = obj_counts['likes']
    print obj_counts_likes
    obj_counts_comments = obj_counts['comments']
    print obj_counts_comments
    obj_counts_repins = obj_counts['repins']
    print obj_counts_repins
    obj_id = data['id']
    print obj_id
    obj_metadata = data['metadata']
    print obj_metadata
    for item1 in obj_metadata:
        print item1
        for item2 in obj_metadata[item1]:
            print item2


    # obj_metadata_link = obj_metadata['link']
    # obj_metadata_link_locale = obj_metadata_link['locale']
    # print obj_metadata_link_locale
    # obj_metadata_link_title = obj_metadata_link['title']
    # print obj_metadata_link_title
    # obj_metadata_link_site_name = obj_metadata_link['site_name']
    # print obj_metadata_link_site_name
    # obj_metadata_link_description = obj_metadata_link['description']
    # print obj_metadata_link_description
    # obj_metadata_link_favicon = obj_metadata_link['favicon']
    # print obj_metadata_link_favicon


    # # Regular expression
    # rx = re.compile('[^a-zA-Z0-9_\'.!,]')
    # obj_bio = rx.sub(' ', data['bio']).strip()
    # print obj_bio
    # print ("==========================================================================================================")
    # writer.writerow({'pin': obj_pin, 'bio': obj_bio, 'first_name': obj_first_name, 'last_name': obj_last_name,
    #                  'account_type': obj_account_type, 'url': obj_url, 'created_at': obj_created_at, 'id': obj_id,
    #                  'count_pins': obj_counts_pins, 'count_following': obj_counts_following,
    #                  'count_followers': obj_counts_followers, 'count_boards': obj_counts_boards,
    #                  'count_likes': obj_counts_likes,
    #                  'image_url': obj_image_url, 'image_width': obj_image_width, 'image_height': obj_image_height})



with open('user_data_try1.csv', 'w') as csvfile:
    fieldnames = ['pin', 'bio', 'first_name', 'last_name', 'account_type', 'url', 'created_at', 'id',
                  'count_pins', 'count_following', 'count_followers', 'count_boards', 'count_likes',
                  'image_url', 'image_width', 'image_height']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for uname in pin_list:
        # Calling search function
        search_user(uname, token_ex)
# search_user(pin_ex, token_ex)