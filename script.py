from bs4 import BeautifulSoup
import requests
import csv

soucre = requests.get('http://coreyms.com').text
soup=BeautifulSoup(soucre,'lxml')

csv_file=open('cms_scrape.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Headline','Summary','Video link'])

article =soup.find_all('article')

for post in article:
    headline=post.h2.a.text
    summary=post.find('div',class_='entry-content').p
    print(headline)
    print()
    print(summary.text)
    print()

    try:
        video=post.find('iframe',class_='youtube-player')['src'].split('/')[4].split('?')[0]
        video_link=f'https://youtube.com/watch?v={video}'
    except Exception as e:
        video_link=None
    print(video_link)
    print()
    print()
    csv_writer.writerow([headline,summary,video_link])

csv_file.close()


# print(article.prettify())
# print(match)

# string='shakil hossen and tawhidul islam'

# list=string.split(' ')
# print(list)
# new_string=' '.join(list)
# print(new_string)