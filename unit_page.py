import bs4
import requests

BASE_URL = "https://www.kalerkantho.com/online/business/2015/11/05/287200"
page = requests.get(BASE_URL)

soup = bs4.BeautifulSoup(page.content, 'html.parser')



newsTitle = soup.find_all("h2")[0].getText()
print(newsTitle)
article_text = soup.find("div", {"class": "some-class-name2"})

all_paragraphs = article_text("p")

news_content = ""

for paragraph in all_paragraphs:
    news_content += paragraph.getText()

#print(news_content)