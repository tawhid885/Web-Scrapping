from bs4 import BeautifulSoup
import requests

with open('index.html') as html_file:
    soup =BeautifulSoup(html_file,'lxml')

match=soup.title

print(match)
