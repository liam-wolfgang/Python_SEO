# import pandas to download a keyword level report from semrush
import pandas as pd
import cloudscraper
from bs4 import BeautifulSoup

keywords = pd.read_excel ('./assets/wolfgang_keywords.xlsx')

# 1 Importing the data from Semrush
low_hanging = keywords[keywords['Position'] < 15]
low_hanging_list = low_hanging.values.tolist()

dict_urls = {}
for urls in low_hanging_list:
    if urls[6] in dict_urls:
        dict_urls[urls[6]] += [[urls[0], urls[1], urls[3]]]
    else:
        dict_urls[urls[6]] = [[urls[0], urls[1], urls[3]]]


# 2 - Scraping the URLs and finding the occurrences
scraper = cloudscraper.create_scraper()

for key, values in dict_urls.items():
    print(str(key))

    html = scraper.get(key, headers = {"User-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    soup = BeautifulSoup(html.text)

    metatitle = (soup.find('title')).get_text()
    metadescription = soup.find('meta', attrs={'name': 'description'})["content"]
    h1 = [a.get_text() for a in soup.find_all('h1')]
    h2 = [a.get_text() for a in soup.find_all('h2')]
    paragraph = [a.get_text() for a in soup.find_all('p')]


