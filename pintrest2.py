# importing packages
import requests
import csv
from bs4 import BeautifulSoup

# Calling URL
##########################################################################################
################Please change the url below and run this python script####################
##########################################################################################
url = "https://in.pinterest.com/pin/188658671869121272/activity/"
##########################################################################################
##########################################################################################
##########################################################################################
print("================================================================")
print("url                      =", url)
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

mainFeed = soup.find("div", class_="feedMain")
if mainFeed!=None:
    # Pin Link
    pinLink = mainFeed.find("div", class_="pinImage").find("a").get("href")
    print("Pin Link                 = ", pinLink)
    # Pin Image
    pinImage = mainFeed.find("div", class_="pinImage").find("img").get("src")
    print("Pin Image                = ", pinImage)
    print("================================================================")

    for activity in soup.find("div", class_="feedItems").find_all("div", class_="activityItem"):

        userProfile = activity.find("div", class_="userProfile")
        if userProfile!=None:
            # user Profile Link
            userProfileLink = userProfile.find("a").get("href")
            print("user Profile Link        =", userProfileLink)
            # user Profile Image
            userProfileImage = userProfile.find("img").get("src")
            print("user Profile Image       =", userProfileImage)
            # userActivity = activity.find("div", class_="activitySummary").find("div", class_="userActivity")

        userActivity = activity.find("div", class_="userActivity")
        if (userActivity!=None):
            # user Activity Link
            userActivityLink = userActivity.find("a").get("href")
            print("user Activity Link       =", userActivityLink)
            # user Full Name
            userFullName = userActivity.find("h2", class_="userFullName").text.strip()
            print("user Full Name           =", userFullName)

        boardSummary = activity.find("div", class_="boardSummary")
        if (boardSummary!=None):
            # board Link
            boardLink = boardSummary.find("a").get("href")
            print("board Summary Link       =", boardLink)
            # board Images
            boardImages = boardSummary.find_all("img")
            for image in boardImages:
                boardImage = image.get("src")
                print("boardImage               =", boardImage)

            boardActivityBottom = boardSummary.find("div", class_="boardActivityBottom")
            if boardActivityBottom!=None:
                # board Link2
                boardLink2 = boardActivityBottom.find("a").get("href")
                print("board Link 2             =", boardLink2)
                # board Name
                boardName = boardActivityBottom.find("h2", class_="boardName").text.strip()
                print("board Name               =", boardName)
                # boardPinCount
                boardPinCount = boardActivityBottom.find("div", class_="boardPinCount").text.strip()
                print("boardPinCount            =", boardPinCount)
        print("----------------------------------------------------------------")
    print("================================================================")
print("End program!!")
