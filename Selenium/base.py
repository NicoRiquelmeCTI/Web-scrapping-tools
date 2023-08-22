from selenium import webdriver
import pandas as pd

website = "https://www.audible.com/search"
# FOR MAC
#path = "/home/nrc/uc/Web-scrapping-tools/bin/chromedriver-win64/chromedriver.exe"
#driver = webdriver.Chrome(path)

# FOR LINUX
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)


## Open driver windows in the desired website
driver.get(website)
driver.maximize_window()

## your bot Code goes here
container = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[5]/div/div[2]/div[4]/div/div')
products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')

Titles = []
Authors = []
for product in products:
    Titles.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)
    Authors.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)

df_books = pd.DataFrame({'Title': Titles, 'Author': Authors})
df_books.to_csv('books.csv', index=False)
## Close driver window
driver.quit()
