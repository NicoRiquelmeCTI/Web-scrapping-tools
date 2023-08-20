from bs4 import BeautifulSoup
import requests

domain = "https://subslikescript.com/"

#print(soup.prettify())

def write_content(site):
    site = f"{domain}/{site}"
    result = requests.get(site)
    content = result.text

    soup = BeautifulSoup(content, "lxml")
    title = soup.find("h1").get_text()
    transcript = soup.find("div", {"class": "full-script"}).get_text(strip=True, separator="\n")
    print(transcript)

    ## Write transcript in a text file
    with open(f'results/{title}', "w") as file:
        file.write(transcript)
    file.close()

def get_links(tag, domain):

    links = []
    site = f"{domain}/{tag}"
    result = requests.get(site)
    content = result.text
    box = BeautifulSoup(content, "lxml").find("ul", {"class": "scripts-list"})
    for link in box.find_all("a", href=True):
        links.append(link['href'])
    return(links)

#write_content("movie/First_Contact-24070610")

links = get_links("movies", domain)
for link in links:
    write_content(link)