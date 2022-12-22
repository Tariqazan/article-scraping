import requests
from bs4 import BeautifulSoup
from database import save_to_database

liputan_data = []

def liputan_scrap():
    url = "https://www.liputan6.com/crypto"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    articles = soup.find_all('article')

    for i in range(len(articles)):
        anchor_tag = articles[i].find_all('a',{'class':'articles--iridescent-list--text-item__title-link'})
        try:
            link = anchor_tag[0].get('href')
        except:
            pass
        title_tag = articles[i].find_all('span',{'class':'articles--iridescent-list--text-item__title-link-text'})
        try:
            title = title_tag[0].text
        except:
            pass
        news_detail = requests.get(link)
        news = BeautifulSoup(news_detail.content, 'html.parser')
        description = news.find_all('div',{'class':'article-content-body__item-content'})
        image = news.find_all('picture')
        img = image[0].find_all('img')
        img_src = img[0].get('src')
        data = {
            "title":title,
            "link":link,
            "description":description,
            "img_src":img_src
        }
        title_string = str(title)
        save_to_database(title_string, str(link), str(description), str(img_src))
        liputan_data.append(data)
    return liputan_data