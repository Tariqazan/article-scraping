import requests
from bs4 import BeautifulSoup

from database import save_to_database


suara_data = []

def suara_scrap():
    url = "https://www.suara.com/tag/kripto"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    links = soup.find_all('a',{'class':'ellipsis3'})


    for i in range(len(links)):
        title = links[i].text
        link = links[i].get('href')
        news_detail = requests.get(link)
        news = BeautifulSoup(news_detail.content, 'html.parser')
        description = news.find_all('article',{'class':'content-article'})
        image = news.find_all('img',{'width':'653'})
        img_src = image[0].get('src')
        data = {
            "title":title,
            "link":link,
            "description":description,
            "img_src":img_src
        }
        title_string = str(title)
        save_to_database(title_string, str(link), str(description), str(img_src))
        suara_data.append(data)
    return suara_data