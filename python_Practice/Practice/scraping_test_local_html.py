from bs4 import BeautifulSoup
import requests

with open('../resource/simple.html')as html_file:
    soup= BeautifulSoup(html_file, 'lxml')

match = soup.title.text

match1 =soup.div


match2 =soup.find('div', class_ ='footer')

article =soup.find('div', class_ ='article')

headline =article.h2.a.text

summary =article.p.text


for article  in soup.find_all('div', class_ ='article'):
    headline =article.h2.a.text
    print(headline)
    summary =article.p.text
    print(summary)
    print()