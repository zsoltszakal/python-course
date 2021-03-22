from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
FORM_WEB = "https://docs.google.com/forms/d/e/1FAIpQLScbMBWRtz-JIMfteQAASbyemKx1z1c1FyFVgmh3aDnWK_z10A/viewform?usp=sf_link"
ZILLOW_WEB = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

response = requests.get(url=ZILLOW_WEB,
                        headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
                            "Accept-Language": "en-US,en;q=0.9,hu;q=0.8,it;q=0.7"} )
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

prices = soup.findAll(name="div", class_="list-card-price")
price_list = [price.text.rsplit('+', 1)[0].rsplit('/', 1)[0].rsplit(' ', 1)[0] for price in prices]
print(price_list)

addresses = soup.findAll(name="address", class_="list-card-addr")
address_list = [address.text for address in addresses]

print(address_list)

DAT_LINK = "https://www.zillow.com/"
links = soup.findAll(name="a", class_="list-card-img")
link_list = [str(DAT_LINK) + str(link.get("href")) for link in links]



chrome_driver_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(FORM_WEB)
#
for n in range(len(price_list)):
    time.sleep(2)

    address_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address_field.send_keys(address_list[n])

    price_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_field.send_keys(price_list[n])

    link_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_field.send_keys(link_list[n])

    time.sleep(1)
    button = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div/span")
    button.click()
    time.sleep(1)
    button_back = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    button_back.click()
