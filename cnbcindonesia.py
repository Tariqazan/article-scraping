import requests
from bs4 import BeautifulSoup

from database import save_to_database


cnbcindonesia_data = []

def cnbcindonesia_scrap():
    url = "https://www.cnbcindonesia.com/search?query=crypto"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    articles = soup.find_all('article')


    for i in range(len(articles)):
        anchor_tag = articles[i].find('a')
        link = anchor_tag.get('href')
        title = articles[i].find('h2').text
        news_detail = requests.get(link)
        news = BeautifulSoup(news_detail.content, 'html.parser')
        description = news.find_all('div',{'class':'detail_text'})
        image = news.find_all('div',{'class':'media_artikel'})
        img_src = image[0].find('img').attrs['src']
        data = {
                "title":title,
                "link":link,
                "description":description,
                "img_src":img_src
            }
        title_string = str(title)
        save_to_database(title_string, str(link), str(description), str(img_src))
        cnbcindonesia_data.append(data)
    return cnbcindonesia_data
    