from selenium import webdriver
import pandas as pd

website = "https://www.audible.com/search"
path = "/Users/nrc/Downloads/chromedriver-mac-x64/chromedriver"
driver = webdriver.Chrome(path)
## Open driver windows in the desired website
driver.get(website)
driver.maximize_window()

## your bot Code goes here
container = driver.find_element_by_xpath('//div[@class="adbl-impression-container"]')
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
