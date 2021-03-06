# coding=utf-8
import ChromeSettings,LoginPage,RemoveMessages,RemovePhoto,UnFollow
from time import sleep
import platform
from getpass import getpass

def onYazi():
    print("", "=" * 50, "\n",
          "#", " " * 46, "#", "\n",
          "#", " " * 14, "Sakir Bey", " " * 14, "#", "\n",
          "#", " " * 6, "Premium İnsta Yönetim ", " " * 6, "#", "\n",
          "#", " " * 46, "#", "\n",
          "=" * 50)

def _input(message, in_type=str):
        while True:
            try:
                return in_type(input(message))
            except:
                print("Türlerine göre değerleri giriniz...")
                pass

def driverUp(chromedriver_path,mobile_emulator):
    chrome = ChromeSettings.ChromeSettings(chromedriver_path,mobile_emulator)
    mobileDriver = chrome.mobileDriver()
    return mobileDriver

def loginPage(driver,username,password):
    LoginPage.LoginPage(driver, "https://www.instagram.com/", username, password).loginPage()

def closeDriver(driver):
    driver.close()

def deletedMessages(driver,count):
    delMes=RemoveMessages.RemoveMessages(driver,count)
    delMes.goMessagePage()
    #delMes.startDeletedMessages()

def deletedPhoto(driver,count):
    defPho=RemovePhoto.RemovePhoto(driver, count)
    defPho.goToProfile()
    #defPho.deletedPhoto()

def unFollow(driver,count):
    unFol=UnFollow.UnFollow(driver,count)
    unFol.goToProfile()
    unFol.goToFollowerList()
    #unFol.unfollow()

if __name__=='__main__':
    chromedriver_path = "/usr/local/bin/chromedriver"

    os=platform.system().lower()
    if os=="darwin": mobile_emulator="iPhone 6"
    else: mobile_emulator="Google Nexus 5"

    onYazi()
    username = _input("Instagram kullanıcı adınız ..: ").lower()
    password = getpass("Senin İnstagram şifren gir ..: ")
    count=_input("Silinecek mesaj veya resim sayısını girin ..: ",int)
    choice=_input("Ne yapmak istediğini seç... \n"
                  "1 - Mesajları Silme \n"
                  "2 - Resim Silme \n"
                  "3 - Takipçi Çıkarma\n"
                  "seçim ..:  ", int)

    driver=driverUp(chromedriver_path,mobile_emulator)
    loginPage(driver,username,password)

    if choice==1:
        deletedMessages(driver,count)
    if choice==2:
        deletedPhoto(driver,count)
    if choice==3:
        unFollow(driver,count)
    sleep(5)
    closeDriver(driver)















