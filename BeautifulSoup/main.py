from bs4 import BeautifulSoup
import requests

web = "https://subslikescript.com/movie/First_Contact-24070610"
result = requests.get(web)
content = result.text

soup = BeautifulSoup(content, "lxml")
print(soup.prettify())