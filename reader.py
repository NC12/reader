# Filename: reader.py
# Author: Ng Cheryl
# Created: 20130401
# Modified: 20130401
# Description: program to convert RSS XML news feed to JSON 
from xml.dom import minidom
import re
import urllib.request
import json

# get XML RSS feed
response = urllib.request.urlopen("http://www.dhs.sg/rss/what%2527s-new%3F-19.xml")
xml = response.read()
# get all XML as a string
xml_data = minidom.parseString(xml).getElementsByTagName('channel')

# get all items
parts = xml_data[0].getElementsByTagName('item')
pdata = []
# loop all items
for part in parts:
    # get title
    title = part.getElementsByTagName('title')[0].firstChild.nodeValue.strip()
    # get link
    link = part.getElementsByTagName('link')[0].firstChild.nodeValue.strip()
    # get description
    description = part.getElementsByTagName('description')[0].firstChild.wholeText.strip()
    description = re.sub("<[^>]*>", "", description)
    description = description[:-10]
    # display info
    pdata.append({"title":title, "link":link, "description":description})
    print("\n".join([title, link, description, ""]))
##  print (pdata)
##  print(type(pdata))

encoded = json.dumps(pdata, sort_keys=True, indent=2)
outfile = open("DATA.JSON", encoding="utf-8", mode="a")
outfile.write(encoded)
outfile.close()

