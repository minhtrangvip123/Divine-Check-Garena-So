from google_speech import Speech
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import datetime

page_link = ['https://divineshop.vn/garena-520', 'https://divineshop.vn/garena-500', 'https://divineshop.vn/garena-2400']
price = [520, 500, 1000]

print(datetime.datetime.now())
for index, i in enumerate(page_link):
	page_response = requests.get(i)

	page_content = BeautifulSoup(page_response.content, "html.parser")

	# print(page_content)

	product_names = page_content.findAll("div", attrs={"class" : "text-wrap"})
   
	# Còn hàng
	if product_names:
		if product_names[1].span.text == "Còn hàng":
			text = "Có hàng " + str(price[index]) + " rồi đại vương ơiiiii"
			lang = "vi"
			# speech = Speech(text, lang)
			# speech.play()
			
# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4
	
def test_answer2():
    assert inc(5) == 6

test_answer()
test_answer2()