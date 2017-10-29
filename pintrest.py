# importing packages
import requests
import csv
from bs4 import BeautifulSoup

# Calling URL
url = "https://in.pinterest.com/pin/29625310029334758/activity/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
#####################################################################################
# for item in soup.find_all('div', class_="pinImage"):
# 	print(item)
# 	print("-----------------------------------------------")
#
for item in soup.find_all('div', class_="pinImage"):
    for item1 in item.find_all('img'):
        pinImage = (item1.get("src"))
count1 = 0
count2 = 0
for item in soup.find_all('div', class_="feedItems"):
    count1 +=1
    for item1 in item.find_all('div', class_="activityItem"):
        # userProfile = item1.find('div', class_="userProfile").find('img')
        # userName = item1.find('div', class_="userProfile").find('img').get("alt")
        # userImage = userProfile.get("src")
        # print(userName, "    ", userImage)
        userLink = item1.find('div', class_="userActivity").find('a').get("href")
        userFullName = item1.find('div', class_="userActivity").find('h2', class_="userFullName").text
        print(userLink,"    ",userFullName)
        # print(item1.find('div', class_="boardSummary").prettify())
        # boardLink = item1.find('div', class_="boardSummary").find('a').get("href")
        # for item2 in item1.find('div', class_="boardSummary").find('div', class_="Collage Module gatorFeed tiles").find_all('div', class_="item"):
        #     boardImage = item2.find('img').get("src")
        # print("--------------------------------------")
        # print(item1.find('div',class_="boardActivityBottom"))
        # AA = item1.find('div',class_="boardActivityBottom")
        # print(item1.find('div', class_="boardActivityBottom").find('a').get("href"))
        # print(AA)
        # print("--------------------------------------")
        # print(AA.find('a').get("href"))
        # print(item1.find('div',class_="boardActivityBottom").find('h2', class_="boardName").text)
        # print("--------------------------------------")
        count2 += 1
        print("%%%%%%%%%%%%%%%", count1 ," ", count2 , "%%%%%%%%%%%%%%%")


#####################################################################################
# Writing a csv

with open("pintrest_data.txt", "w") as data:
    FileWriter = csv.writer(data)
    FileWriter.writerow(["pinImage", "userName" , "userImage"])

with open("pintrest_data.txt", "a") as data:
    FileWriter = csv.writer(data)
    FileWriter.writerow([pinImage, userName, userImage])
data.close()









