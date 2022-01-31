import time
import smtplib
from traceback import print_exception
import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import os

# Terminal Penceresini Temizleyen fonksiyon

def clear():
    """
        Bu fonksiyon terminal penceresini ilk haline getirir.
    """
    # İşletim Sistemi Windows ise
    if os.name == 'nt':
        _ = os.system('cls')
    # İşletim Sistemi MacOS ise
    elif os.name == 'mac':
        _ = os.system('clear')
    # İşletim Sistemi Linux ise
    elif os.name == 'posix':
        _ = os.system('clear')
    # Yabancı bir işletim sistemi ise
    else:
        _ = os.system('clear')


url = 'https://www.hepsiburada.com/xiaomi-redmi-note-10s-128-gb-6-gb-ram-xiaomi-turkiye-garantili-p-HBCV00000FO61M'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50'}


page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
span = soup.find(id='offering-price')
content = span.attrs.get('content')
price = float(content)

    
target_mail = str(input("Gönderilecek Mail Adresini Giriniz: "))
subject_mail = str(input("Mailin Başlığını Giriniz: "))
      

# Gmail email sunucusuna bağlanıyoruz
def send_mail(title):
    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login('pricetracking11@gmail.com', 'jwdlsvhkncwinqpq')

        mesaj = MIMEMultipart()
        mesaj["From"] = "pricetracking11@gmail.com"          # Gönderen
        mesaj['To'] = target_mail           # Gönderilen
        mesaj["Subject"] = subject_mail    # Konusu

        body = 'Note 10 S Güncel Fiyatı '+ content +'\n\n Şu Linkten Ulaşabilirsiniz => ' + url





        body_text = MIMEText(body, "plain")  #
        mesaj.attach(body_text)

        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        print("Mail başarılı bir şekilde gönderildi.")
        mail.close()

# Eğer mesaj gönderirken hata olursa, hata mesajını konsole yazdırıyorum.
    except:
        print("Hata:", sys.exc_info()[0])
    finally:
        mail.quit()



def check_price():
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='product-name').get_text().strip()
    print(title)
    span = soup.find(id='offering-price')
    content = span.attrs.get('content')
    price = float(content)
    print('Güncel Fiyat: "%s"' % content)
    if price < 4000:
        send_mail(title)


while (1):
    clear()
    check_price()
    print("Son Güncelleme: %s" % time.ctime())
    time.sleep(60*5)
