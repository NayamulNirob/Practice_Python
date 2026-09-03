import csv
from bs4 import BeautifulSoup
import requests



source= requests.get('https://www.patreon.com/coreyms')
print(source.status_code)
source_html = source.text
soup= BeautifulSoup(source_html, 'lxml')
# print(soup.prettify())

csv_file = open('../cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['spanClass'])



# article = soup.find('sc-48ef06c2-0')
# print(article.prettify())

# matcher =soup.find('div',class_='sc-b8e5eaa3-0')
# print(matcher.prettify())

for matcher in soup.find_all('div',class_='sc-b8e5eaa3-0'):
    # print(matcher.prettify())
    spanClass = matcher.find_all('span')
    print(spanClass)
    print()


    csv_writer.writerow([spanClass])

csv_file.close()