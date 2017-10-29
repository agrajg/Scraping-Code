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
    data = json.load(json_obj)
    for item1 in data:
        # print item1, " = " , data[item1]
        # for item2a in data[item1]:
        #     print item2a, " = ", data[item1][item2a]
        #     # print "TYPE = ", type(data[item1][item2a])

        print 'attribution', " = ", data[item1]['attribution']


        for item2b in data[item1]['creator']:
            print item2b, " = " , data[item1]['creator'][item2b]
            # print "TYPE = ", type(data[item1]['creator'][item2b])

        print 'url', " = ", data[item1]['url']

        for item2c in data[item1]['media']:
            print item2c, " = " , data[item1]['media'][item2c]
            # print "TYPE = ", type(data[item1]['media'][item2c])

        print 'id', " = ", data[item1]['id']
        print 'note', " = ", data[item1]['note']
        print 'color', " = ", data[item1]['color']
        print 'link', " = ", data[item1]['link']

        for item2d in data[item1]['board']:
            print item2d, " = " , data[item1]['board'][item2d]
            # print "TYPE = ", type(data[item1]['board'][item2d])

        for item2e in data[item1]['image']:
            print item2e, " = " , data[item1]['image'][item2e]
            # print "TYPE = ", type(data[item1]['image'][item2e])

        for item2f in data[item1]['counts']:
            print item2f, " = ", data[item1]['counts'][item2f]
            # print "TYPE = ", type(data[item1]['counts'][item2f])

        print 'original_link', " = ", data[item1]['original_link']

        for item2g in data[item1]['metadata']:
            print item2g, " = ", data[item1]['metadata'][item2g]
            # print "TYPE = ", type(data[item1]['metadata'][item2g])
            for item3a in data[item1]['metadata'][item2g]:
                print item3a, " = ", data[item1]['metadata'][item2g][item3a]
                # print "TYPE = ", type(data[item1]['metadata'][item2g][item3a])

with open('pin_data_try1.csv', 'w') as csvfile:
    fieldnames = ['pin', 'bio', 'first_name', 'last_name', 'account_type', 'url', 'created_at', 'id',
                  'count_pins', 'count_following', 'count_followers', 'count_boards', 'count_likes',
                  'image_url', 'image_width', 'image_height']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for uname in pin_list:
        # Calling search function
        search_user(uname, token_ex)
# search_user(pin_ex, token_ex)