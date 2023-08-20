from bs4 import BeautifulSoup
import requests

## 1 - Define the website target
domain = "https://subslikescript.com/"
## 2 - Define section or category
site = "movies"
site = f"{domain}/{site}"
result = requests.get(site)
content = result.text
soup = BeautifulSoup(content, "lxml")


# This function will write the content of the page in a text file
def write_content(site):
    site = f"{domain}/{site}"
    result = requests.get(site)
    content = result.text

    soup = BeautifulSoup(content, "lxml")
    title = soup.find("h1").get_text()
    transcript = soup.find("div", {"class": "full-script"}).get_text(strip=True, separator="\n")
    #print(transcript)

    ## Write transcript in a text file
    with open(f'results/{title}', "w") as file:
        file.write(transcript)
    file.close()

# This function will get all the links from a directory page
def get_links(tag, domain, page = 1):

    try:
        links = []
        site = f"{domain}/{tag}?page={page}"
        result = requests.get(site)
        content = result.text
        box = BeautifulSoup(content, "lxml").find("ul", {"class": "scripts-list"})
        for link in box.find_all("a", href=True):
            links.append(link['href'])
            #print(links[:-1])
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    except AttributeError as err:
        raise SystemExit(err)
    return(links)

#write_content("movie/First_Contact-24070610")

#PAGINATION
# This function will explore all the pages of a directory
def pagination():
    pagination = soup.find("ul", {"class": "pagination"})
    last_page = int(pagination.find_all("li", {"class": "page-item"})[-2].text)
    links = []
    for page in range(1, last_page+1):
        links.extend(get_links("movies", domain, page))
        print(len(links))
    return links

# Here we will save all the links in a list
links = pagination()

# Here we will write output the content of each page
# for link in links:
#     write_content(link)