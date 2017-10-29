# importing packages
import urllib2
import requests
import csv
import json
import re


example_board = "laurenkc17/weddings"
token = "AXE3eFg3YRL1p-3XKpPMcpGQuGKnFKhBNBPS8mxDfVOF9MBAhQAAAAA"
example_url = "https://api.pinterest.com/v1/boards/laurenkc17/weddings/pins/?access_token=AXE3eFg3YRL1p-3XKpPMcpGQuGKnFKhBNBPS8mxDfVOF9MBAhQAAAAA&fields=id%2Clink%2Cnote%2Curl%2Cattribution%2Cboard%2Ccolor%2Ccounts%2Ccreated_at%2Ccreator%2Cimage%2Cmedia%2Cmetadata%2Coriginal_link"


def search_board(board, token):
    print ("==========================================================================================================")
    url = 'https://api.pinterest.com/v1/boards/'+ board +'/pins/?access_token=' + token +'&fields=id%2Clink%2Cnote%2Curl%2Cattribution%2Cboard%2Ccolor%2Ccounts%2Ccreated_at%2Ccreator%2Cimage%2Cmedia%2Cmetadata%2Coriginal_link'
    print "URL = " + url
    json_obj = urllib2.urlopen(url)
    print ("----------------------------------------------------------------------------------------------------------")
    page_data = json.load(json_obj)



    # print page_data
    for item1 in page_data:
        print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
        print "     item1 = ", item1, "|    type(page_data[item1]) = ", type(page_data[item1])
        print ("----------------------------------------------------------------------------------------------------------")
        print ("----------------------------------------------------------------------------------------------------------")
        # print page_data[item1]
        for item2 in page_data[item1]:
            print "item2 = ",item2
            print "type(item2)= ", type(item2), "type(page_data[item1][item2])= ",type(page_data[item1][item2])
        print ("----------------------------------------------------------------------------------------------------------")
        print ("----------------------------------------------------------------------------------------------------------")
    # print ("----------------------------------------------------------------------------------------------------------")
    # for item2 in page_data['data']:
    #     print item2




    # print "--------------------------------------------------------------------------------------------------------------------------"
    # for item1 in data:
    #     print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
    #     print "     item1 = ", item1
    #     # print "       data[item1] = ", data[item1]
    #     for item2 in data[item1]:
    #         print "-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - "
    #         print "         item2 = ", item2,"          type(item2) = ", type(item2)
    #         print "         data[item1][item2]=", data[item1][item2]
        #     if type(item2) is dict:
        #         print "pins"
        #     if type(item2) is unicode:
        #         print item2
        #         print data[item1][item2]



    #     # print item1, " = " , data[item1]
    #     # for item2a in data[item1]:
    #     #     print item2a, " = ", data[item1][item2a]
    #     #     # print "TYPE = ", type(data[item1][item2a])
    #
    #     print 'attribution', " = ", data[item1]['attribution']
    #
    #
    #     for item2b in data[item1]['creator']:
    #         print item2b, " = " , data[item1]['creator'][item2b]
    #         # print "TYPE = ", type(data[item1]['creator'][item2b])
    #
    #     print 'url', " = ", data[item1]['url']
    #
    #     for item2c in data[item1]['media']:
    #         print item2c, " = " , data[item1]['media'][item2c]
    #         # print "TYPE = ", type(data[item1]['media'][item2c])
    #
    #     print 'id', " = ", data[item1]['id']
    #     print 'note', " = ", data[item1]['note']
    #     print 'color', " = ", data[item1]['color']
    #     print 'link', " = ", data[item1]['link']
    #
    #     for item2d in data[item1]['board']:
    #         print item2d, " = " , data[item1]['board'][item2d]
    #         # print "TYPE = ", type(data[item1]['board'][item2d])
    #
    #     for item2e in data[item1]['image']:
    #         print item2e, " = " , data[item1]['image'][item2e]
    #         # print "TYPE = ", type(data[item1]['image'][item2e])
    #
    #     for item2f in data[item1]['counts']:
    #         print item2f, " = ", data[item1]['counts'][item2f]
    #         # print "TYPE = ", type(data[item1]['counts'][item2f])
    #
    #     print 'original_link', " = ", data[item1]['original_link']
    #
    #     for item2g in data[item1]['metadata']:
    #         # print item2g, " = ", data[item1]['metadata'][item2g]
    #         # print "TYPE = ", type(data[item1]['metadata'][item2g])
    #         for item3a in data[item1]['metadata'][item2g]:
    #             print item3a, " = ", data[item1]['metadata'][item2g][item3a]
    #             # print "TYPE = ", type(data[item1]['metadata'][item2g][item3a])



search_board(example_board, token)
