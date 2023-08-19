from bs4 import BeautifulSoup
import requests

web = "https://subslikescript.com/movie/First_Contact-24070610"
result = requests.get(web)
content = result.text

soup = BeautifulSoup(content, "lxml")
#print(soup.prettify())
title = soup.find("h1").get_text()
transcript = soup.find("div", {"class": "full-script"}).get_text(strip=True, separator="\n")
print(transcript)

## Write transcript in a text file
with open(f'{title}', "w") as file:
    file.write(transcript)

file.close()