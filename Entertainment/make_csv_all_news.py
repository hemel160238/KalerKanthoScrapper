import bs4
import requests
import csv

URL_LINK = 'remaining_link.csv'
CSV_LINK = 'business_kalerkantho.csv'

def append_to_csv(row):

    global CSV_LINK

    with open(CSV_LINK, mode='a', newline='', encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            news_article_writer.writerow(row)

    #news_article_writer.close()    

    pass


def get_title_and_content(url):
    BASE_URL = url
    page = requests.get(BASE_URL)

    soup = bs4.BeautifulSoup(page.content, 'html.parser')



    newsTitle = soup.find_all("h2")[0].getText()
    #print(newsTitle)
    article_text = soup.find("div", {"class": "some-class-name2"})

    all_paragraphs = article_text("p")

    news_content = ""

    for paragraph in all_paragraphs:
        news_content += paragraph.getText()

    #print(news_content)

    input_array = [newsTitle, news_content, 'economy']

    append_to_csv(input_array)




    pass



with open(URL_LINK) as unit_url_csv:
    readCSV = csv.reader(unit_url_csv)

    for row in readCSV:
        print(row)
        get_title_and_content(row[0])