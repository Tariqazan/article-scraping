import requests
from bs4 import BeautifulSoup
from database import save_to_database

tempo_data = []

def tempo_scrap():
    url = "https://www.tempo.co/search?q=kripto"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    links = soup.find_all('h2',{'class':'title'})

    for i in range(len(links)):
        anchor_tag = links[i].find_all('a')
        link = anchor_tag[0].get('href')
        title = anchor_tag[0].text
        news_detail = requests.get(link)
        news = BeautifulSoup(news_detail.content, 'html.parser')
        description = news.find_all('div',{'class':'detail-in'})
        image = news.find_all('figure',{'class':'margin-bottom-xs'})
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
        tempo_data.append(data)
    return tempo_data