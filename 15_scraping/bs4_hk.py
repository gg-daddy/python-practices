import pprint

import requests
from bs4 import BeautifulSoup


def extract_news(links, subtexts):
    result = []
    for link, subtext in zip(links, subtexts):
        score = subtext.select_one(".score")
        if score:
            points = int(score.text.replace(" points", ""))
            if points > 99:
                result.append(
                    (
                        link.text,
                        link.select_one("a").get("href"),
                        points,
                    )
                )
    return sorted(result, key=lambda x: x[2], reverse=True)


def get_hk_news_from_page(news_url):
    resp = requests.get(news_url)
    soup = BeautifulSoup(resp.text, "html.parser")
    links = soup.select(".titleline")
    subtexts = soup.select(".subtext")
    news = extract_news(links, subtexts)
    pprint.pprint(news)


if __name__ == "__main__":
    for i in range(1, 11):
        # 观察网页地址的变化，找到规律
        get_hk_news_from_page(f"https://news.ycombinator.com/news?p={i}")
