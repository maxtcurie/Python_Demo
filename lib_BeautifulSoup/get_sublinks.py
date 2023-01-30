#from: https://pythonprogramminglanguage.com/get-links-from-webpage/
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request("https://nstx.pppl.gov/nstx/SpecFit/")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)