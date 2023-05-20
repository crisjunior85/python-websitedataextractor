#web scraping, extracting data from a website
#need two lib: pip bs4, pip requests... bs4 stands for beautiful soup
#use in your python shell

import requests
from bs4 import BeautifulSoup

url = "https://www.phantomsandmonsters.com"
r = requests.get(url)
print("r")  #in the shell just type r

soup = BeautifulSoup(r.content, "lxml")

#now in the website youve chosen, click inspect and see which html tag the article blog is located

title = soup.find_all("h2", {"class": "post-title"})
print("title")

title1 = title[0].getText() #if you want to get the text only
print("title1") #printing in pyhton shell dont need ""

for t in title:  #gives a list of titles of the website
  print(t.getText())
