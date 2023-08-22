from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

try:
    # Initialize the webdriver (you should have the appropriate driver executable in your PATH)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    # Open the webpage containing the title elements you want to hover over
    url = "https://factual.afp.com/list/all/37881/all/all/95"
    driver.get(url)
    cokies_button = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
    cokies_button.click()

    # Find the title elements you want to hover over
    title_elements = driver.find_elements_by_xpath('//div[contains(@class, "card-body")]')

    # Create an empty list to store the generated URLs
    url_list = []
    last_page = driver.find_element_by_xpath('/html/body/nav/div/div/div[3]/ul/li[3]/a')
    last_page.click()
    current_link = driver.current_url
    last_page_number = current_link.split("=")[1]
    print(f'Total pages: {last_page_number}')
    first_page_button = driver.find_element_by_xpath('/html/body/nav/div/div/div[1]/ul/li[1]/a')
    first_page_button.click()

    for page in range(1, int(last_page_number)):
        try:
            print(f'Currently scrapping page {page}')
            # Loop through the title elements and hover over each one to generate the URL
            for i in range(len(title_elements)):
                try:
                    # Encuentra nuevamente los elementos en cada iteración
                    title_elements = driver.find_elements_by_xpath('//div[contains(@class, "card-body")]')
                    # Realiza clic en el elemento de título
                    # Obtén el elemento de título actual
                    title_element = title_elements[i]
                    title_element.click()
                    
                    # Espera un poco para que la página cargue (ajusta el tiempo si es necesario)
                    driver.implicitly_wait(3)  # Espera 3 segundos (puedes ajustar este valor)
                    # Obtén la URL actual después de hacer clic
                    destination_url = driver.current_url
                    print(destination_url)
                    # Agrega la URL de destino a la lista
                    url_list.append(destination_url)
                    
                    # Regresa a la página anterior
                    driver.back()
                except (ElementClickInterceptedException, StaleElementReferenceException) as e:
                    print(f"Error al interactuar con el elemento: {e}")
        
            next_page_button = driver.find_element_by_xpath('/html/body/nav/div/div/div[3]/ul/li[1]/a')
            next_page_button.click()
            driver.implicitly_wait(3)
        except Exception as e:
            print(f'Error en la página {page}: {e}')

finally:
    # Close the webdriver
    driver.quit()

    # Print the list of generated URLs
    print(url_list)
    df_links = pd.DataFrame({'link': url_list})
    df_links.to_csv('links.csv', index=False)
