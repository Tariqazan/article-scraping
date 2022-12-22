import requests
from bs4 import BeautifulSoup
from database import save_to_database


detik_data = []


def detik_scrap():
    url = "https://www.detik.com/search/searchall?query=kripto"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    articles = soup.find_all('article')

    for i in range(len(articles)):
        anchor_tag = articles[i].find_all('a')
        link = anchor_tag[0].get('href')
        title_tag = articles[i].find_all('h2',{'class':'title'})
        title = title_tag[0].text
        news_detail = requests.get(link)
        news = BeautifulSoup(news_detail.content, 'html.parser')
        description = news.find_all('div',{'class':'detail__body-text'})
        image = news.find_all('figure')
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
        detik_data.append(data)
    return detik_data