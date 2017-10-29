# importing packages
import urllib2
import requests
import csv
import json
import re

board_list = ["laurenkc17/weddings", "mandamandagirl/kicks-giggles"]
example_board = "laurenkc17/weddings"
token = "AXE3eFg3YRL1p-3XKpPMcpGQuGKnFKhBNBPS8mxDfVOF9MBAhQAAAAA"
example_board_pins_url = "https://api.pinterest.com/v1/boards/laurenkc17/weddings/pins/?access_token=AXE3eFg3YRL1p-3XKpPMcpGQuGKnFKhBNBPS8mxDfVOF9MBAhQAAAAA&fields=id%2Clink%2Cnote%2Curl%2Cattribution%2Cboard%2Ccolor%2Ccounts%2Ccreated_at%2Ccreator%2Cimage%2Cmedia%2Cmetadata%2Coriginal_link"
example_board_url = "https://api.pinterest.com/v1/boards/mandamandagirl/kicks-giggles/?access_token=AXE3eFg3YRL1p-3XKpPMcpGQuGKnFKhBNBPS8mxDfVOF9MBAhQAAAAA&fields=id%2Cname%2Curl%2Ccounts%2Ccreated_at%2Ccreator%2Cdescription%2Cimage%2Cprivacy%2Creason"


with open('boardpindata.csv', 'wb') as csvfile:
    fieldnames = ['board_name',
                  'board_privacy',
                  'board_url',
                  'board_created_at',
                  'board_creator',
                  'board_creator_url',
                  'board_creator_first_name',
                  'board_creator_last_name',
                  'board_creator_id',
                  'board_id',
                  'board_reason',
                  'board_counts',
                  'board_counts_pins',
                  'board_counts_collaborators',
                  'board_counts_followers',
                  'board_image',
                  'board_image_60x60_url',
                  'board_description',
                  'pin_attribution',
                  'pin_creator',
                  'pin_creator_url',
                  'pin_creator_first_name',
                  'pin_creator_last_name',
                  'pin_creator_id',
                  'pin_url',
                  'pin_media',
                  'pin_created_at',
                  'pin_original_link',
                  'pin_id',
                  'pin_note',
                  'pin_color',
                  'pin_link',
                  'pin_board',
                  'pin_board_url',
                  'pin_board_id',
                  'pin_board_name',
                  'pin_image',
                  'pin_image_original_url',
                  'pin_image_original_width',
                  'pin_image_original_height',
                  'pin_counts',
                  'pin_counts_likes',
                  'pin_counts_comments',
                  'pin_counts_repins',
                  'pin_metadata']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for board_id in board_list:
        board_pins_url = "https://api.pinterest.com/v1/boards/" + board_id + "/pins/?access_token="+ token +"&fields=id%2Clink%2Cnote%2Curl%2Cattribution%2Cboard%2Ccolor%2Ccounts%2Ccreated_at%2Ccreator%2Cimage%2Cmedia%2Cmetadata%2Coriginal_link"
        print "URL = ", board_pins_url
        board_pins_json_obj = urllib2.urlopen(board_pins_url)
        print ("------------------------------------------------------------------------------------------------------")
        board_pins_page_data = json.load(board_pins_json_obj)
        for item1 in board_pins_page_data['data']:
            print("========================================================")
            # Collecting boards data
            board_url = "https://api.pinterest.com/v1/boards/"+ board_id +"/?access_token="+ token +"&fields=id%2Cname%2Curl%2Ccounts%2Ccreated_at%2Ccreator%2Cdescription%2Cimage%2Cprivacy%2Creason"
            print "URL = ", board_url
            board_json_obj = urllib2.urlopen(board_url)
            print ("------------------------------------------------------------------------------------------------------")
            board_page_data = json.load(board_json_obj)

            board_name = board_page_data['data']['name']
            print 'name', " = ", type(board_page_data['data']['name']), " = ", board_page_data['data']['name'] is not None, " = ", board_page_data['data']['name']
            if board_name is None:
                board_name = " "

            board_privacy = board_page_data['data']['privacy']
            print 'privacy', " = ", type(board_page_data['data']['privacy']), " = ", board_page_data['data']['privacy'] is not None, " = ", board_page_data['data']['privacy']
            if board_privacy is None:
                board_privacy = " "

            board_url = board_page_data['data']['url']
            print 'url', " = ", type(board_page_data['data']['url']), " = ", board_page_data['data']['url'] is not None, " = ", board_page_data['data']['url']
            if board_url is None:
                board_url = " "

            board_created_at = board_page_data['data']['created_at']
            print 'created_at', " = ", type(board_page_data['data']['created_at']), " = ", board_page_data['data']['created_at'] is not None, " = ", board_page_data['data']['created_at']
            if board_created_at is None:
                board_created_at = " "

            board_creator = board_page_data['data']['creator']
            print 'creator', " = ", type(board_page_data['data']['creator']), " = ", board_page_data['data']['creator'] is not None, " = ", board_page_data['data']['creator']
            if board_creator is None:
                board_creator = " "

            board_creator_url = board_page_data['data']['creator']['url']
            print 'creator_url', " = ", type(board_page_data['data']['creator']['url']), " = ", board_page_data['data']['creator']['url'] is not None, " = ",board_page_data['data']['creator']['url']
            if board_creator_url is None:
                board_creator_url = " "

            board_creator_first_name = board_page_data['data']['creator']['first_name']
            print 'creator_first_name', " = ", type(board_page_data['data']['creator']['first_name']), " = ", board_page_data['data']['creator']['first_name'] is not None, " = ", board_page_data['data']['creator']['first_name']
            if board_creator_first_name is None:
                board_creator_first_name = " "

            board_creator_last_name = board_page_data['data']['creator']['last_name']
            print 'creator_last_name', " = ", type(board_page_data['data']['creator']['last_name']), " = ", board_page_data['data']['creator']['last_name'] is not None, " = ", board_page_data['data']['creator']['last_name']
            if board_creator_last_name is None:
                board_creator_last_name = " "

            board_creator_id = board_page_data['data']['creator']['id']
            print 'creator_id', " = ", type(board_page_data['data']['creator']['id']), " = ", board_page_data['data']['creator']['id'] is not None, " = ", board_page_data['data']['creator']['id']
            if board_creator_id is None:
                board_creator_id = " "




            board_id = board_page_data['data']['id']
            print 'id', " = ", type(board_page_data['data']['id']), " = ", board_page_data['data']['id'] is not None," = " ,board_page_data['data']['id']
            if board_id is None:
                board_id = " "

            board_reason = board_page_data['data']['reason']
            print 'reason', " = ", type(board_page_data['data']['reason']), " = ", board_page_data['data']['reason'] is not None, " = ", board_page_data['data']['reason']
            if board_reason is None:
                board_reason = " "

            board_counts = board_page_data['data']['counts']
            print 'counts', " = ", type(board_page_data['data']['counts']), " = ", board_page_data['data']['counts'] is not None, " = ", board_page_data['data']['counts']
            if board_counts is None:
                board_counts = " "

            board_counts_pins = board_page_data['data']['counts']['pins']
            print 'counts_pins', " = ", type(board_page_data['data']['counts']['pins']), " = ", \
            board_page_data['data']['counts']['pins'] is not None, " = ", board_page_data['data']['counts']['pins']
            if board_counts_pins is None:
                board_counts_pins = " "

            board_counts_collaborators = board_page_data['data']['counts']['collaborators']
            print 'counts_collaborators', " = ", type(board_page_data['data']['counts']['collaborators']), " = ", \
            board_page_data['data']['counts']['collaborators'] is not None, " = ", board_page_data['data']['counts']['collaborators']
            if board_counts_collaborators is None:
                board_counts_collaborators = " "

            board_counts_followers = board_page_data['data']['counts']['followers']
            print 'counts_followers', " = ", type(board_page_data['data']['counts']['followers']), " = ", \
            board_page_data['data']['counts']['followers'] is not None, " = ", board_page_data['data']['counts']['followers']
            if board_counts_followers is None:
                board_counts_followers = " "

            board_image = board_page_data['data']['image']
            print 'image', " = ", type(board_page_data['data']['image']), " = ", board_page_data['data']['image'] is not None, " = ", board_page_data['data']['image']
            if board_image is None:
                board_image = " "

            board_image_60x60_url = board_page_data['data']['image']['60x60']['url']
            print 'image_60x60_url', " = ", type(board_page_data['data']['image']['60x60']['url']), " = ", board_page_data['data'][
                                                                                     'image']['60x60']['url'] is not None, " = ", \
            board_page_data['data']['image']['60x60']['url']
            if board_image_60x60_url is None:
                board_image_60x60_url = " "

            board_description = board_page_data['data']['description']
            print 'description', " = ", type(board_page_data['data']['description']), " = ", board_page_data['data']['description'] is not None, " = ", board_page_data['data']['description']
            if board_description is None:
                board_description = " "

            # Collecting pins data
            pin_attribution = item1['attribution']
            print 'attribution', " = ", type(item1['attribution']), " = ", item1['attribution'] is not None, " = ", item1['attribution']
            if pin_attribution is None:
                pin_attribution = " "

            pin_creator = item1['creator']
            print 'creator', " = ", type(item1['creator']), " = ", item1['creator'] is not None, " = ", item1['creator']
            if pin_creator is None:
                pin_creator = " "

            pin_creator_url = item1['creator']['url']
            print 'creator_url', " = ", type(item1['creator']['url']), " = ", item1['creator']['url'] is not None, " = ", item1['creator']['url']
            if pin_creator_url is None:
                pin_creator_url = " "

            pin_creator_first_name = item1['creator']['first_name']
            print 'creator_first_name', " = ", type(item1['creator']['first_name']), " = ", item1['creator'][
                                                                                  'first_name'] is not None, " = ", \
            item1['creator']['first_name']
            if pin_creator_first_name is None:
                pin_creator_first_name = " "

            pin_creator_last_name = item1['creator']['last_name']
            print 'creator_last_name', " = ", type(item1['creator']['last_name']), " = ", item1['creator'][
                                                                                  'last_name'] is not None, " = ", \
            item1['creator']['last_name']
            if pin_creator_last_name is None:
                pin_creator_last_name = " "

            pin_creator_id = item1['creator']['id']
            print 'creator_id', " = ", type(item1['creator']['id']), " = ", item1['creator'][
                                                                                  'id'] is not None, " = ", \
            item1['creator']['id']
            if pin_creator_id is None:
                pin_creator_id = " "



            pin_url = item1['url']
            print 'url', " = ", type(item1['url']), " = ", item1['url'] is not None, " = ", item1['url']
            if pin_url is None:
                pin_url = " "

            pin_media = item1['media']
            print 'media', " = ", type(item1['media']), " = ", item1['media'] is not None, " = ", item1['media']
            if pin_media is None:
                pin_media = " "

            pin_created_at = item1['created_at']
            print 'created_at', " = ", type(item1['created_at']), " = ", item1['created_at'] is not None, " = ", item1['created_at']
            if pin_created_at is None:
                pin_created_at = " "

            pin_original_link = item1['original_link']
            print 'original_link', " = ", type(item1['original_link']), " = ", item1['original_link'] is not None, " = ", item1[
                'original_link']
            if pin_original_link is None:
                pin_original_link = " "

            pin_id = item1['id']
            print 'id', " = ", type(item1['id']), " = ", item1['id'] is not None, " = ", item1['id']
            if pin_id is None:
                pin_id = " "

            # pin_note = item1['note']
            rx = re.compile('[^a-zA-Z0-9_\'.!,]')
            pin_note = rx.sub(' ', item1['note']).strip()
            print 'note', " = ", type(item1['note']), " = ", item1['note'] is not None, " = ", item1['note']
            if pin_note is None:
                pin_note = " "

            pin_color = item1['color']
            print 'color', " = ", type(item1['color']), " = ", item1['color'] is not None, " = ", item1['color']
            if pin_color is None:
                pin_color = " "

            pin_link = item1['link']
            print 'link', " = ", type(item1['link']), " = ", item1['link'] is not None, " = ", item1['link']
            if pin_link is None:
                pin_link = " "

            pin_board = item1['board']
            print 'board', " = ", type(item1['board']), " = ", item1['board'] is not None, " = ", item1['board']
            if pin_board is None:
                pin_board = " "

            pin_board_url = item1['board']['url']
            print 'board_url', " = ", type(item1['board']['url']), " = ", item1['board']['url'] is not None, " = ", item1['board']['url']
            if pin_board_url is None:
                pin_board_url = " "

            pin_board_id = item1['board']['id']
            print 'board_id', " = ", type(item1['board']['id']), " = ", item1['board']['id'] is not None, " = ", \
            item1['board']['id']
            if pin_board_id is None:
                pin_board_id = " "

            pin_board_name = item1['board']['name']
            print 'board_name', " = ", type(item1['board']['name']), " = ", item1['board']['name'] is not None, " = ", \
            item1['board']['name']
            if pin_board_name is None:
                pin_board_name = " "



            pin_image = item1['image']
            print 'image', " = ", type(item1['image']), " = ", item1['image'] is not None, " = ", item1['image']
            if pin_image is None:
                pin_image = " "

            pin_image_original_url = item1['image']['original']['url']
            print 'image_original_url', " = ", type(item1['image']['original']['url']), " = ", item1['image']['original']['url'] is not None, " = ", item1['image']['original']['url']
            if pin_image_original_url is None:
                pin_image_original_url = " "

            pin_image_original_width = item1['image']['original']['width']
            print 'image_original_width', " = ", type(item1['image']['original']['width']), " = ", \
            item1['image']['original']['width'] is not None, " = ", item1['image']['original']['width']
            if pin_image_original_width is None:
                pin_image_original_width = " "

            pin_image_original_height = item1['image']['original']['height']
            print 'image_original_height', " = ", type(item1['image']['original']['height']), " = ", \
            item1['image']['original']['height'] is not None, " = ", item1['image']['original']['height']
            if pin_image_original_height is None:
                pin_image_original_height = " "




            pin_counts = item1['counts']
            print 'counts', " = ", type(item1['counts']), " = ", item1['counts'] is not None, " = ", item1['counts']
            if pin_counts is None:
                pin_counts = " "

            pin_counts_likes = item1['counts']['likes']
            print 'counts_likes', " = ", type(item1['counts']['likes']), " = ", item1['counts']['likes'] is not None, " = ", item1['counts']['likes']
            if pin_counts_likes is None:
                pin_counts_likes = " "

            pin_counts_comments = item1['counts']['comments']
            print 'counts_comments', " = ", type(item1['counts']['comments']), " = ", item1['counts'][
                                                                                    'comments'] is not None, " = ", \
            item1['counts']['comments']
            if pin_counts_comments is None:
                pin_counts_comments = " "

            pin_counts_repins = item1['counts']['repins']
            print 'counts_repins', " = ", type(item1['counts']['repins']), " = ", item1['counts'][
                                                                                    'repins'] is not None, " = ", \
            item1['counts']['repins']
            if pin_counts_repins is None:
                pin_counts_repins = " "



            pin_metadata = item1['metadata']
            print 'metadata', " = ", type(item1['metadata']), " = ", item1['metadata'] is not None, " = ", item1['metadata']
            if pin_metadata is None:
                pin_metadata = " "

            writer.writerow({'board_name': board_name,
                             'board_privacy': board_privacy,
                             'board_url': board_url,
                             'board_created_at': board_created_at,
                             'board_creator': board_creator,
                             'board_id': board_id,
                             'board_reason': board_reason,
                             'board_counts': board_counts,
                             'board_counts_pins': board_counts_pins,
                             'board_counts_collaborators': board_counts_collaborators,
                             'board_counts_followers': board_counts_followers,
                             'board_image': board_image,
                             'board_image_60x60_url': board_image_60x60_url,
                             'board_description': board_description,
                             'pin_attribution': pin_attribution,
                             'pin_creator': pin_creator,
                             'pin_creator_url': pin_creator_url,
                             'pin_creator_first_name': pin_creator_first_name,
                             'pin_creator_last_name': pin_creator_last_name,
                             'pin_creator_id': pin_creator_id,
                             'pin_url': pin_url,
                             'pin_media': pin_media,
                             'pin_created_at': pin_created_at,
                             'pin_original_link': pin_original_link,
                             'pin_id': pin_id,
                             'pin_note': pin_note,
                             'pin_color': pin_color,
                             'pin_link': pin_link,
                             'pin_board': pin_board,
                             'pin_board_url': pin_board_url,
                             'pin_board_id': pin_board_id,
                             'pin_board_name': pin_board_name,
                             'pin_image': pin_image,
                             'pin_image_original_url': pin_image_original_url,
                             'pin_image_original_width': pin_image_original_width,
                             'pin_image_original_height': pin_image_original_height,
                             'pin_counts': pin_counts,
                             'pin_counts_likes': pin_counts_likes,
                             'pin_counts_comments': pin_counts_comments,
                             'pin_counts_repins': pin_counts_repins,
                             'pin_metadata': pin_metadata})
