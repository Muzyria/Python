import requests
from bs4 import BeautifulSoup
from time import sleep


list_card_url = []

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/110.0.0.0 Safari/537.36"}

for count in range(1, 8):
    # sleep(1)
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")  # html.parser

    data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
    # print(data)

    for i in data:
        # name = i.find("h4", class_="card-title").text.replace("\n", "")
        # # print(name)
        # price = i.find("h5").text
        # # print(price)
        # url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")
        # # print(url_img)
        # print(name, price, url_img, sep="\n")
        card_url = "https://scrapingclub.com" + i.find("a").get("href")
        list_card_url.append(card_url)


for card_url in list_card_url:
    response = requests.get(card_url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")  # html.parser

    data = soup.find("div", class_="card mt-4 my-4")
    print(data)
