import requests
import bs4

BASE_URL = "https://www.kalerkantho.com/online/business/18"
page = requests.get(BASE_URL)

soup = bs4.BeautifulSoup(page.content, 'html.parser')

all_a = soup.find_all("a", {"class": "title"})

for a_tag in all_a:
    print(a_tag["href"])
