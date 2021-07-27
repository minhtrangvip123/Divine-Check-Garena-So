from google_speech import Speech
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import datetime

page_link = ['https://divineshop.vn/garena-520', 'https://divineshop.vn/garena-500', 'https://divineshop.vn/garena-2400']
price = [520, 500, 1000]

while True:
    print(datetime.datetime.now())
    for index, i in enumerate(page_link):
        page_response = requests.get(i)

        page_content = BeautifulSoup(page_response.content, "html.parser")

        # print(page_content)

        product_names = page_content.findAll("div", attrs={"class" : "text-wrap"})
        try:
            print((product_names[1].span.text))
        except IndexError as err:
            print("Page chua mo")
            continue
        # Còn hàng
        if product_names[1].span.text == "Còn hàng":
            text = "Có hàng " + str(price[index]) + " rồi đại vương ơiiiii"
            lang = "vi"
            speech = Speech(text, lang)
            speech.play()

    time.sleep(60)