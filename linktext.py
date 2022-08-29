import requests
from bs4 import BeautifulSoup
page = requests.get("https://phptravels.com/blog/how-can-video-marketing-help-your-travel-agencies-website-conversion-rate")
soup = BeautifulSoup(page.content, 'html.parser')
ele=soup.find_all('a')
f=open("test1.txt",'w')
for i in ele:
    a=i.get('href')
    f.write(a)
    f.write('\n')
f.close()
