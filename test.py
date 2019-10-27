import bs4
import requests

base_address = "https://www.kalerkantho.com"
BASE_URL = "https://www.kalerkantho.com/online/business/18"
page = requests.get(BASE_URL)

soup = bs4.BeautifulSoup(page.content, 'html.parser')


newsArticleDivs = soup.find_all("div", {"class": "col-xs-12 col-sm-6 col-md-6 n_row"})


for newsArticle in newsArticleDivs:
    a_tag = newsArticle.find("a")
    news_link = a_tag['href']
    complete_url = base_address + news_link[1:]
    print(complete_url)