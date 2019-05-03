from bs4 import BeautifulSoup
import json

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os

# Url yang dituju
url = "https://www.google.com"
weather_forecast = os.getenv('weather forecast', 'weather forecast')

# Membuat driver/’jembatan’ ke Firefox
driver = webdriver.Chrome()
driver.get(url)

# Mencari tag HTML yang digunakan untuk memasukkan username, lalu
 # nilainya akan diisi dengan string dari variabel USERNAME
search_input = driver.find_element_by_name('q')
search_input.send_keys(weather_forecast)
search_input.submit()

# Tunggu paling lama 5 detik hingga browser mengembalikan halaman
# baru
driver.implicitly_wait(5)

button_wob_rain = driver.find_element_by_id('wob_rain').click()


url = driver.current_url
print(url)

# driver.quit()