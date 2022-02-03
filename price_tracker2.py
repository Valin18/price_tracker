# Kütüphaneleri Projeye Dahil Ediyorum
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
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For MacOS
    elif os.name == 'mac':
        _ = os.system('clear')
    # For Linux
    elif os.name == 'posix':
        _ = os.system('clear')
    # For Any System's
    else:
        _ = os.system('clear')


url = 'https://www.hepsiburada.com/xiaomi-redmi-note-10s-128-gb-6-gb-ram-xiaomi-turkiye-garantili-p-HBCV00000FO61M'
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 11; M2101K7BG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 GSA/13.2.19.23.arm64 OpaScreenful/0'}


page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
span = soup.find(id='offering-price')
content = span.attrs.get('content')
price = float(content)

# Kullanıcıdan Mail Adresi Ve Gönderilecek Mail İçin Bir Başlık Alıyorum
target_mail = str(input("Gönderilecek Mail Adresini Giriniz: "))
subject_mail = str(input("Mailin Başlığını Giriniz: "))
asking_price = float(input('Istenilen Fiyat: '))

# Gmail email sunucusuna bağlanıyorum
def send_mail(title):
    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login('pricetracking11@gmail.com', 'ayeddbodytzuhluq')

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


# Fiyat Kontrolü Yapan Fonksiyon
def check_price():
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='product-name').get_text().strip()
    print(title)
    span = soup.find(id='offering-price')
    content = span.attrs.get('content')
    price = float(content)
    print('Güncel Fiyat: "%s"' % content)
    if price < asking_price:
        send_mail(title)

# İşlemimi Döngüye Alarak check_price() Fonksiyonum İle Fiyat Kontrolü Yapıyorum
while (1):
    clear()
    check_price()
    print("Son Güncelleme: %s" % time.ctime())
    time.sleep(30*2)

   
#                                                                                                                                                           Maded By Valin
