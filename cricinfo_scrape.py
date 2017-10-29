import requests
from bs4 import BeautifulSoup

url ="http://www.espncricinfo.com/ci/engine/current/match/65268.html"
r= requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


print soup.prettify()
soup.find_all("a")

for link in soup.find_all("a"):
	print link.text ,link.get("href")




g_data = soup.find_all("td", {"class": "playerName" })
for item in g_data:
	print item.text


#end of the
