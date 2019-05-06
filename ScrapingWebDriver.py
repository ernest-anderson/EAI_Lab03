from bs4 import BeautifulSoup
import json
import requests

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

# Tunggu paling lama 5 detik hingga browser mengembalikan halaman baru
driver.implicitly_wait(5)

# Pindah ke tab curah hujan
button_to_web = driver.find_element_by_xpath("//span[@jscontroller='ICK5Cb']/table[@class='di8g3 YGvGmb']/tbody/tr/td[@class='ZK9O6d']/a").click()

button_hourly_weather = driver.find_element_by_xpath("//span[@id='looking_ahead_link']/a[@data-from-string='today-looking-ahead_hourly']").click()

#
if __name__ == '__main__':
	# Ambil dokumen HTML dari halaman sekarang
	document = requests.get(driver.current_url)
	print(driver.current_url)
	
	# Parse teks dokumen HTML ke objek DOM menggunakan Beautiful Soup
	dom_object = BeautifulSoup(document.text, features = "html.parser")

	# Peroleh referensi ke semua tag ‘div’ dengan class ‘vk_gy vk_sh wob-dtl’
	##table_tag = dom_object.find(name='table', attrs={'class':'twc-table'})

	# Ambil semua thead dari tag ‘table’
	##thead_tr_tag = table_tag.find(name='thead').findAll(name='tr')
	# Ambil semua th dari tag ‘table’
	th_tag = dom_object.find(name='th', attrs={'id': 'temp'})

	# Ambil semua thead dari tag ‘table’
	##tbody_tr_tag = table_tag.find(name='tbody').findAll(name='tr')
	# Ambil semua td dari tag ‘table’
	##td_tag = dom_object.findAll(name='td')

	# Ambil semua konten teks dari setiap tag ‘th’
	print("##########################")
	print(th_tag.text)
	description_contents = th_tag.text
	##description_contents = [description.text for description in th_tag]

	# Ambil semua konten teks dari setiap tag ‘td’
	##data_contents = [data.text for data in td_tag]

	# Lalu siapkan struktur data dictionary untuk menyimpan setiap teks
	descriptions = [{'description': content} for content in description_contents]
	output_file = open('output_weather.json', 'w', encoding='utf8')

 	# Buat format JSON yang membungkus setiap konten teks
	json_output = {
		'source': driver.current_url,
		'data': json.dumps(descriptions)
	}
	
	# Tulis ke sebuah berkas
	output_file.write(json.dumps(json_output))
	output_file.flush()
	output_file.close()

driver.quit()