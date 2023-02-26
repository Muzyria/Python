import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/?page=1"


response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")  # html.parser

data = soup.find("div", class_="col-lg-4 col-md-6 mb-4")
# print(data)

name = data.find("h4", class_="card-title").text.replace("\n", "")
# print(name)
price = data.find("h5").text
# print(price)
url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
# print(url_img)

print(name, price, url_img, sep="\n")
