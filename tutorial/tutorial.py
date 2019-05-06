#!/usr/bin/env python3
from bs4 import BeautifulSoup
import json
import requests

SCELE_URL = 'https://scele.cs.ui.ac.id'
if __name__ == '__main__':
 # Ambil dokumen HTML dari laman depan Scele
 document = requests.get(SCELE_URL)
 
 # Parse teks dokumen HTML ke objek DOM menggunakan Beautiful Soup
 dom_object = BeautifulSoup(document.text, features = "html.parser")
 
 # Peroleh referensi ke semua tag ‘div’ dengan class ‘posting fullpost’
 post_divs = dom_object.findAll(name='div', attrs={'class': 'posting fullpost'})
 
 # Ambil semua konten teks dari setiap tag ‘div’
 post_contents = [post.text for post in post_divs]
 
 # Lalu siapkan struktur data dictionary untuk menyimpan setiap teks
 posts = [{'content': content} for content in post_contents]
 output_file = open('output.json', 'w', encoding='utf8')
 
 # Buat format JSON yang membungkus setiap konten teks
 json_output = {
  'source': SCELE_URL,
  'data': json.dumps(posts)
 }

# Tulis ke sebuah berkas
output_file.write(json.dumps(json_output))
output_file.flush()
output_file.close()