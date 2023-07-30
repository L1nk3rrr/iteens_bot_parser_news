import requests
from bs4 import BeautifulSoup

site_link = "https://www.pravda.com.ua"

r = requests.get(url=site_link + "/news", verify=True)
soup = BeautifulSoup(r.content, "html.parser")

# [{header, link, body_text}, {header, link, body_text}, {header, link, body_text}, ...]
news_list = []

for news in soup.select(".article_header > a")[:4]:
    news_text = news.text.strip()
    news_href = news.get("href", "") 
    news_link = site_link + news_href if "http" not in news_href else news_href 

    r_news = requests.get(url=news_link, verify=True)
    soup_news = BeautifulSoup(r_news.content, "html.parser")
 
    body_text = ""
    body_text_list = []
    if "www.pravda" in news_link:
        for p in soup_news.select(".post_text > p"):
            body_text_list.append(f"{p.text.strip()}\n")
        body_text = " ".join(body_text_list)
    elif "www.epravda" in news_link or "www.eurointegration" in news_link:
        for p in soup_news.select(".post__text > p"):
            body_text_list.append(f"{p.text.strip()}\n")
        body_text = " ".join(body_text_list)
    elif "life.pravda" in news_link:
        for p in soup_news.select(".article > p"):
            body_text_list.append(f"{p.text.strip()}\n")
        body_text = " ".join(body_text_list)


    news_list.append({
        "header": news_text, 
        "link": news_link,
        "body_text": body_text,
    })

