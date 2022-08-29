import requests
from bs4 import BeautifulSoup
page = requests.get("https://phptravels.com/blog/how-can-video-marketing-help-your-travel-agencies-website-conversion-rate")
soup = BeautifulSoup(page.content, 'html.parser')
heading=["h1","h2","h3"]
for tags in soup.find_all(heading):
    print(tags.text)