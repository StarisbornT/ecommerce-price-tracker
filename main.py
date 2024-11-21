import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import ssl

url = "https://www.amazon.com/dp/B09TYVYRD9/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
    "Accept-Language": "en-US,en;q=0.5"
}
BUY_PRICE = 200
my_email = "crywallett556@gmail.com"
password1 = "xxikowophmzteoxn"
reciever = "crywallett556@gmail.com"
subject = "Price Update from Amazon"


response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price_element = soup.find(class_="a-offscreen")
title = soup.find(id="productTitle").get_text().strip()
print(title)

if price_element:
    price = price_element.get_text()
    price_without_currency = price.split("$")[1]
    price_as_float = float(price_without_currency)
    print(price_as_float)
    if price_as_float < BUY_PRICE:
        message = f"{title} is now {price}"
        em = EmailMessage()
        em['From'] = my_email
        em['To'] = reciever
        em['Subject'] = subject
        em.set_content(message)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context) as con:
            con.login(my_email, password1)
            con.sendmail(my_email, reciever, em.as_string())
else:
    print("Price not found")