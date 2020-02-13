import urllib.request
from bs4 import BeautifulSoup
import time

url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')

results = soup.select(".list_body dl dt:nth-child(2) a")

for result in results:
    print("제목 : ", result.string)
    url_article = result.attrs["href"]
    response = urllib.request.urlopen(url_article)
    soup_article = BeautifulSoup(response, "html.parser")
    content = soup_article.select_one("#articleBodyContents")
    output = ""
    for item in content.contents:
        description = str(item).strip()
        if description in "":
            continue
        if description[0] not in ["<", "/"]:
            output += item
    print(output.replace(" 본문 내용  TV플레이어", ""))    
    time.sleep(1)