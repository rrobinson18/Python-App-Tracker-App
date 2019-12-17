import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.amazon.com/Apple-MacBook-13-inch-128GB-Storage/dp/B07V49JVNH/ref=sr_1_1_sspa?crid=1AFXR8ABV55QT&keywords=macbook+pro&qid=1576595024&sprefix=%2Caps%2C2347&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTjRNNDJIQjFMSUNEJmVuY3J5cHRlZElkPUEwNDA3MDMxMzZHTFgzTDNPS0Y3UiZlbmNyeXB0ZWRBZElkPUEwNDE3NDk5T0kwSk1XTTAzUFRCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 1.700):
        send_mail()

    print(converted_price)
    print(title.strip())


    if(converted_price > 1.700):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('robinson.rakesha@gmail.com', 'bgofylkrfjgnuqrh')

    subject = 'Price fell down!'

    body = 'Check the amazon link https://www.amazon.com/Apple-MacBook-13-inch-128GB-Storage/dp/B07V49JVNH/ref=sr_1_1_sspa?crid=1AFXR8ABV55QT&keywords=macbook+pro&qid=1576595024&sprefix=%2Caps%2C2347&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTjRNNDJIQjFMSUNEJmVuY3J5cHRlZElkPUEwNDA3MDMxMzZHTFgzTDNPS0Y3UiZlbmNyeXB0ZWRBZElkPUEwNDE3NDk5T0kwSk1XTTAzUFRCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'robinson.rakesha@gmail.com',
        'robinson.rakesha@icloud.com',
        msg
    )

    print('Hey email has been sent!')

    server.quit()

check_price()
