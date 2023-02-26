import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/110.0.0.0 Safari/537.36"}


def download(url):
    resp = requests.get(url, stream=True)
    with open(rf"C:\Git_Muzyria\Stepik\scraping\image\{url.split('/')[-1]}", "wb") as file:
        for value in resp.iter_content(1024*1024):
            file.write(value)


def get_url():
    for count in range(1, 8):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")  # html.parser
        data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")

        for i in data:
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url


for card_url in get_url():
    response = requests.get(card_url, headers=headers)
    # sleep(1)
    soup = BeautifulSoup(response.text, "lxml")  # html.parser

    data = soup.find("div", class_="card mt-4 my-4")
    name = data.find("h3", class_="card-title").text
    price = data.find("h4").text
    text = data.find("p", class_="card-text").text
    url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
    download(url_img)
    print(name, price, text, url_img, sep="\n")
