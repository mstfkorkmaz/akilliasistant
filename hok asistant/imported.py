from gtts import gTTS 

import speech_recognition as sr 

import os
from os import system as komut

import wikipedia 

import webbrowser 

import smtplib 

import datetime 
import time 
import sys

import cv2 

import random

import pyowm 

import psutil 

import fbchat 
from getpass import getpass 
import pygame

import pyperclip


from subprocess import Popen

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googlesearch import search

from youtube_search import YoutubeSearch 


from pydub import AudioSegment 
from pydub.playback import play

buyukAlfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
kucukAlfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

def lower(command:str): 
    newText = str()
    for i in command:
        if i in command:
            if i in buyukAlfabe:
                index = buyukAlfabe.index(i)
                newText += kucukAlfabe[index]
            else:
                newText += i
    return newText

def talkUS(audio):
    print("Asistan: " + audio +  f" : {time.strftime('%X')}")
    tts = gTTS(text=audio, lang="tr", slow = False)
    tts.save("audio.mp3") 
    sound = AudioSegment.from_file("audio.mp3")  
    play(sound)



def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        komut("clear") 
        print("Diğer komut için hazırım") 
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration= 1) 
        audio = r.listen(source,phrase_time_limit = 8) 
    print("Dur.") 
    try:
        command = r.recognize_google(audio,language="tr") 
        command = lower(command) 
        print("Söylenen: " + command + f" : {time.strftime('%X')}" +"\n") 

    except sr.UnknownValueError: 
        print("Son komutunuz anlaşılmadı.")
        command = myCommand();

    return command.lower()


def searchOnGoogle(gl_ans,outputList): 
    for output in search(gl_ans,tld = "co.in",lang = "tr", num = 10, stop = 5 , pause = 2): 
        outputList.append(output) 
    return outputList

def openLink(outputList):
    webbrowser.open(outputList[1])  

def searchHow(ans_how,outpuLst):
    for outpt in search(ans_how + " nasıl yapılır",tld = "co.in",lang = "tr", num = 10, stop = 5 , pause = 2):
        print(outpt)
        outpuLst.append(outpt)

    return outpuLst

def linkOpen(outpuLst):
    webbrowser.open(outpuLst[1])



def get_size(bytes, suffix="B"):   

    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor



hour = int(datetime.datetime.now().hour)
if hour >= 4 and hour < 12:
    talkUS("Günaydın, size nasıl yardımcı olabilirim?")

elif hour >= 12 and hour < 17:
    talkUS("İyi günler, size nasıl yardımcı olabilirim?")  

else:
    talkUS("İyi akşamlar, size nasıl yardımcı olabilirim?")



def opn_gl():
    gogle = ["google açılıyor","tarayıcınızı açıyorum","hemen açıyorum",
    "tarayıcı açılıyor","çabucak açıyorum","emredersiniz","başım üstüne",
    "bir işide kendin yapsan şaşardım","işte google"]

    talkUS(random.choice(gogle))
    p_google = Popen("google-chrome")

def open_yt():
    ytube = ["işte youtube","youtube açılıyor","karşınızda youtube",
    "youtube açıyorum","emredersin","başım üstüne","kendin açsana",
    "youtube bu aralar ölmüş","trendlerde dizi dolu ama sen bilirsin"]

    talkUS(random.choice(ytube))
    webbrowser.open("https://www.youtube.com.tr")

def open_dc():
    talkUS("Discord açılıyor")
    
    p_dc = Popen("discord")   

def open_wp():
    talkUS("Whatsapp açılıyor")
    p_wp = Popen("whatsdesk")

def open_tlg():
    talkUS("Telegram açılıyor")
    p_tlg = Popen("telegram-desktop")

def open_cal():
    talkUS("Hesap makinesi açılıyor")
    p_cal = Popen("gnome-calculator")

def open_clden():
    talkUS("Takvim açılıyor")
    p_clden = Popen("gnome-calendar")

def open_atom():
    talkUS("Atom editör açılıyor")
    p_atom = Popen("atom")

def open_gedit():
    talkUS("Not defteri açılıyor")
    p_editör = Popen("gedit")

def open_tw():
    talkUS("Hangi yayıncıyı açmalıyım?")
    tw_ans = input("Yayıncı adı giriniz: ")
    tw_lst = ["elraenn","mithrain","Xantares","kendinemüzisyen",
    "jahrein","wtcn","rammus53"]
    

    if tw_ans in tw_lst:
        webbrowser.open("https://www.twitch.tv/" + tw_ans)
    else: 
        talkUS("Böyle bir yayıncıyı tanımıyorum")



def sy_hlo():
    hello = ["hey selam","selam","merhaba","sanada merhaba","hey insan",
    "merhabalar","hoş geldin","seni bekliyordum","bugün ne yapıyorum?",
    "evet seni dinliyorum","seni dinliyorum"]

    talkUS(random.choice(hello))

def sy_fine():
    uok = ["iyiyim","sesini duydum daha iyi oldum","iyiyim sen","iyiyi sen nasılsın",
    "idare ediyorum","keyifsizim sanki","biraz keyifsizim","iyi gidiyor",
    "her şey yolunda seni sormalı"]

    talkUS(random.choice(uok))

def sy_ty():
    thy = ["rica","rica ederim","ne demek","lafımı olur","hiç bir şey",
    "yardımım dokunduysa ne mutlu bana",
    "yardımcı olabildiysem ne mutlu bana","benim için çocuk oyuncağıydı"]

    talkUS(random.choice(thy))

def wh_made():
    speak = '''Merhaba,Ben sizin kişisel sesli asistanınızım Can İlgu
    tarafından geliştirilmekteyim'''
    talkUS(speak)

def tk_nte():
    talkUS("Evet sizi dinliyorum") 
    file1 = open("NoteFile.txt","a") 
    note = myCommand()              
    file1.write(note + "\n")
    file1.close()
    talkUS("Notunuzu yazdım.") 

def rd_nte():
    file1 = open("NoteFile.txt","r") 
    talkUS(file1.read())
    file1.close()
    talkUS("Notlarınızı okudum") 

def dl_nte():
    talkUS("Notlarınızı silmek istediğinizden emin misiniz?") 
    del_ans = myCommand() 
    if "evet" in del_ans or "evet sil" in del_ans:
        file1 = open("NoteFile.txt","r+")
        file1.truncate(0)
        talkUS("Notlarınız başarıyla silindi.")

    if "hayır" in del_ans or "hayır kalsın" in del_ans or "hayır silme" in del_ans:
        talkUS("Notlarınız silinmeyecek.")

def py_musc():
    talkUS("Listeden rasgele bir müzik açıyorum") 
    pygame.mixer.init()
    random_file = "/home/can/Downloads/Musics/"
    musics = ["Ben Fero - Biladerim İcin", "Berkcan - Neresi", "Ezhel - LOLO"]
    random_music = random_file + random.choice(musics) + ".mp3"
    pygame.mixer.music.load(random_music)
    pygame.mixer.music.play()

def py_stp():
    talkUS("Müzik kapatılıyor")
    pygame.mixer.music.stop()

def th_tme():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    talkUS(f"Efendim, şuan saat {strTime} ") 

def th_dy():
    strDay = datetime.datetime.now().strftime("%B %d %A")
    talkUS(f"Bugün günlerden, {strDay} ")

def pc_kpt():
    talkUS("Bilgisayarınız 5 saniye içerisinde kapanacak.")
    time.sleep(5)
    os.system("shutdown now -h") 

def pc_yndn():
    talkUS("Bilgisayarınız yeniden başlatılacak")
    os.system("shutdown -r now") 

def pc_otrm():
    talkUS("Oturumunuz kapatılıyor")
    
    os.system("gnome-session-quit --no-prompt") 

def cl_brwsr():
    talkUS("Tarayıcınız kapanıyor.")
    os.system("pkill firefox") 


def gl_mps():
    talkUS("Nereyi görmek istersiniz?")
    mps_ans = myCommand()
    location = mps_ans
    talkUS("Hemen gösteriyorum")
    p_mps = Popen(["chromium-browser","https://www.google.nl/maps/place/" + location + "/&amp;"])

def wk_pdia():
    talkUS("Hangi konuda bilgi almak istersiniz?")
    wk_ans = myCommand()
    wikipedia.set_lang("tr")
    talkUS("Araştırılıyor")
    results = wikipedia.summary(wk_ans, sentences = 2)
    talkUS(results)

def gl_srch():
    outputList = []
    talkUS("Ne araştırmalıyım?")
    gl_ans = myCommand()
    searchOnGoogle(gl_ans,outputList)
    talkUS("İlgili sayfa açılıyor?")
    openLink(outputList)


def gl_how():
    talkUS("Neyin, nasıl yapıldığını öğrenmek istersin?")
    ans_how = myCommand()
    outpuLst = []
    searchHow(ans_how,outpuLst)
    talkUS("İlgili web sayfası açılıyor")
    linkOpen(outpuLst)

def yt_srch():
    talkUS("Hangi şarkıyı veya videoyu açmamı istersin?")
    yt_ans = myCommand()
    yt_results = YoutubeSearch(yt_ans, max_results=1).to_dict()
    for v in yt_results:
        print('https://www.youtube.com.tr' + v['link'])
        
    talkUS("Aramamda çıkan ilk sonucu açıyorum")
    webbrowser.open('https://www.youtube.com.tr' + v['link'])


def cpu_inf():
    print("="*20, "CPU Bilgi", "="*20) 
    print("Toplam çekirdek:", psutil.cpu_count(logical=True)) 
    cpufreq = psutil.cpu_freq()
    print(f"Anlık Ghz: {cpufreq.current:.2f}Mhz") 
    print("CPU Yüzdelik Kullanımı:") 
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Kullanımı: {psutil.cpu_percent()}%") 
    time.sleep(5) 


def hdd_inf():
    partition_usage = psutil.disk_usage('/') 
    print(f"  Toplam alan: {get_size(partition_usage.total)}")
    print(f"  Kullanılan: {get_size(partition_usage.used)}")
    print(f"  Boşta: {get_size(partition_usage.free)}")
    print(f"  Yüzdelik: {partition_usage.percent}%")
    time.sleep(5)

def ram_inf():
    svmem = psutil.virtual_memory()
    print("="*20, "RAM Kullanımı", "="*20)
    print(f"Toplam: {get_size(svmem.total)}") 
    print(f"Kullanılan: {get_size(svmem.used)}")  
    print(f"Yüzdelik: {svmem.percent}%") 
    time.sleep(5)


def wh_temp():
    owm = pyowm.OWM("API KEY")
    our_loc = owm.weather_at_place("Kyrenia, CY")
    weather = our_loc.get_weather()

    loc_temp = int(weather.get_temperature("celsius")["temp"])
    wind = weather.get_wind()
    humidit = weather.get_humidity()

    talkUS("Hava sıcaklığı " + str(loc_temp) + " derece")
    talkUS("Rüzgar " + str(wind["speed"]) + " kilometre hızında")
    talkUS("Nem oranı ise %" + str(humidit))

def jr_down():
    jr_ans = ["kapanıyorum","hoşçakal iyi günler","hoşçakal","iyi günler","yine beklerim",
    "görüşürüz","görüşmek üzere","tamam iyi günler"]

    talkUS(random.choice(jr_ans))
    sys.exit()

def fb_msg():
    fb_ans = [" merhaba"," hoş geldin"," lütfen şifreni gir"," lütfen şifrenizi giriniz"," şifreniz lütfen",
    " merhaba şifrenizi girmeniz gerekiyor"]

    username = "haspguard" 
    talkUS(username + random.choice(fb_ans))

    
    client = fbchat.Client(username, getpass()) 
    talkUS("Arkadaşınızın adını giriniz.")
    name = str(input("Name: "))  
    friends = client.searchForUsers(name)  
    friend = friends[0] 
    talkUS("Lütfen mesajınızı yazınız.")
    msg = str(input("Message: ")) 
    sent = client.sendMessage(msg, thread_id=friend.uid)
    if sent:
        talkUS("Mesajınız başarıyla gönderilmiştir.") 

def wb_cm():
    talkUS("Kameranız açılıyor")
    print("Çıkış için ESC")
    print("Anlık görüntü almak için SPACE") 
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    video_capture = cv2.VideoCapture(0) 
    img_counter = 0

    while True:
        
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        k = cv2.waitKey(1)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        
        cv2.imshow('FaceDetection', frame)

        if k%256 == 27: 
            break

        elif k%256 == 32:
           
            img_name = "facedetect_webcam_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1


    
    video_capture.release()
    cv2.destroyAllWindows()

def fb_lgn():
    mailname = "" 
    password1 = ""
    class Facebook: 
        def __init__(self,mail,password): 
            self.browser = webdriver.Chrome() 
            self.mail = mailname
            self.password = password1

        def singIn(self): 
            self.browser.get("https://www.facebook.com/login/") 

            try:
                mailnameInput = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='email']")));
                password1Input = self.browser.find_element_by_xpath("//*[@id='pass']")

                mailnameInput.send_keys(self.mail) 
                password1Input.send_keys(self.password)

            except:
                print("Mail/Şifre girilemedi!")
            try:
                fb_lgn = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='loginbutton']")));
                fb_lgn.clik()

            except:
                print("Login butonuna tıklanılmadı!")

    facbk = Facebook(mailname,password1)
    facbk.singIn()

def gthb_lgn():
    gitname = ""
    gitpass = ""
    class Github:
        def __init__(self,gitname,gitpass):
            driver = "/home/can/Downloads/chromedriver" 
            self.browser = webdriver.Chrome(driver)
            self.gitname = gitname
            self.gitpass = gitpass

        def singn(self):
            self.browser.get("https://github.com/login")
            self.browser.maximize_window()
            try:
                gitnameInput = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='login_field']")));
                gitpassInput = self.browser.find_element_by_xpath("//*[@id='password']")

                gitnameInput.send_keys(self.gitname)
                gitpassInput.send_keys(self.gitpass)
            except:
                print("Mail/Şifre girilemedi!")

            try:
                gitLgn = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='login']/form/div[3]/input[8]")));
                gitLgn.click()
            except:
                print("Giriş butonuna tıklanılmadı!")

    githb = Github(gitname, gitpass)
    githb.singn()


def inst_lng():
    email = "deneme"
    password = "deneme"
    class Instagram:
        def __init__(self,email,password):
            self.browser = webdriver.Chrome()
            self.email = email
            self.password = password

        def signIn(self):
            self.browser.get("https://www.instagram.com/accounts/login/")
            self.browser.maximize_window()

            try:
                emailInput = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")));
                passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")

                emailInput.send_keys(self.email)
                passwordInput.send_keys(self.password)

            except:
                print("Mail/Şifre girilemedi!")

            try:
                lgnClick = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button/div")));
                lgnClick.click()


            except:
                print("Login butonuna tıklanılmadı!")

    instgrm = Instagram(email,password)
    instgrm.signIn()

def spd_tst():
    class Speed:
        def __init__(self):
            self.browser = webdriver.Chrome()
            

        def pressButon(self):
            self.browser.get("https://www.speedtest.net/")
            self.browser.maximize_window()
            try:
                butonPress = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='container']/div[2]/div/div/div/div[2]/div[3]/div[1]/a")));
                butonPress.click()

            except:
                print("Bir hata oluştu!")

    sped = Speed()
    sped.pressButon()


def twtt_lgn():
    usernm = ""
    password2 = ""

    class Twitter:
        def __init__(self, usernm, password2):
            self.browser = webdriver.Chrome()
            self.usernm = usernm
            self.password2 = password2

        def twittSing(self):
            self.browser.get("https://twitter.com/login?lang=tr")  
            self.browser.maximize_window()
            
            try:
                usernameInput = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH , "//*[@id='react-root']/div/div/div[1]/main/div/div/form/div/div[1]/label/div[2]/div/input")));
                passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[1]/main/div/div/form/div/div[2]/label/div[2]/div/input")

                usernameInput.send_keys(self.usernm)
                passwordInput.send_keys(self.password2)
            except:
                print("Mail/Şifre girilemedi!")

            try:
                btnSubmit = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div[1]/main/div/div/form/div/div[3]/div/div")));
                btnSubmit.click()

            except:
                print("Giriş butonuna tıklanılmadı!")

            talkUS("Twitter'da bir şeyler aramamı ister misiniz?")
            twtt_ans = myCommand()
            twtt_ans2 = input("Aranacak kelime: ")
            if "evet ara" in twtt_ans or "evet isterim" in twtt_ans or "evet" in twtt_ans or "ara" in twtt_ans or "isterim" in twtt_ans:
                talkUS("Ne aramamı istersiniz?")
                twtt_ans2 = input("Aranacak kelime: ") 
              
                try:
                    searhBtn = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")));
                    searhBtn.send_keys(twtt_ans2)
                    searhBtn.send_keys(Keys.ENTER)  
                
                except:
                    print("Arama çubuğu kullanılamadı!")

                
                try:
                                                                                                
                     lastNews = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div[2]/div[2]/a/div/span")));
                     lastNews.click()
                except:
                    print("En son sekmesine tıklanılmadı!")
        
        
                

            if "hayır" in twtt_ans or "istemiyorum" in twtt_ans or "hayır arama" in twtt_ans:
                talkUS("Twitter artık sizin kontrolünüzde")

    twitterr = Twitter(usernm,password2)
    twitterr.twittSing()





def gl_trns():
    talkUS("Lütfen çevirisini yapmak istediğiniz kelimeyi giriniz") 
    gl_cvr = input("Yabancı Kelimeniz: ")

    class Ceviri:
        def __init__ (self):
            self.browser = webdriver.Chrome()
        def transWord(self):
            self.browser.get("https://www.google.com.tr")
            self.browser.maximize_window()

            try:
                wordTrans = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")));
                wordTrans.send_keys("google translate")

            except:
                print("Arama kısmına google translate yazılamadı!")

            try:
                srchBtn = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")));
                srchBtn.click()

            except:
                prin("Ara butonuna tıklanılmadı!")

            try:
                wrdTrns = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='tw-source-text-ta']")));
                wrdTrns.send_keys(gl_cvr)  

            except:
                print("Yabancı kelime yazılamadı!")

            try:
                Trnsword = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tw-tl']")));
                Trnsword.click()

            except:
                print("Bir hata meydana geldi!")

            try:
                detectLng = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tl_list-search-box']")));
                detectLng.send_keys("Turkish")
                detectLng.send_keys(Keys.ENTER)

            except:
                prin("Hata!")


    trnsword = Ceviri()
    trnsword.transWord()

def fod_rder():
    usrnm = "" 
    pswrd = ""

    class Yemek:
        def __init__(self, usrnm, pswrd):
            self.browser = webdriver.Chrome() 
            self.usrnm = usrnm 
            self.pswrd = pswrd

        def yemekLogin(self):

            self.browser.get("https://www.yemeksepeti.com/kktc")
            self.browser.maximize_window() 
            talkUS("Ne yemek istersiniz?")
            food_ans = input("Yemeğinizn ismi: ")

            try:
                usrnmInput = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='UserName']")));
                pswrdInput = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='password']")));

                usrnmInput.send_keys(self.usrnm)
                pswrdInput.send_keys(self.pswrd)

                lgnBtn = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ys-fastlogin-button']")));
                lgnBtn.click()

            
            
            except:
                print("Hata")
            time.sleep(2) 

        
            try:   
                ctySlct =WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/header/div/div/div/div[2]/span/span[1]/span/span[2]")));
                ctySlct.click()
            except:
                print("Şehir seçme hatası")

    
            try: 
                Slcttown = self.browser.find_element_by_xpath("//*[@id='ys-areaSelector-droparea']/span/span/span[1]/input")
                Slcttown.send_keys(Keys.ENTER)
            except:
                print("Şehir yok!")


            try:

                srchBtn = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/header/div/div/div/div[4]/input")));
                srchBtn.click()
                srchBtn.send_keys(food_ans)
                srchBtn.send_keys(Keys.ENTER)
            except:

                print("Arama yapma hatası ")
        

            try:
                frstFood = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/a/i")));
                frstFood.click()

            except:
                print("Çıkan ilk yemeği seçme hatası!")



            try:
                confrmOrder = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='basket-container']/div[2]/div/div[5]/button")));
                confrmOrder.click()

            except:
                print("Yemek menüsü onaylanıyor lütfen bekleyiniz..")
                foodFrst = self.browser.find_element_by_xpath("//*[@id='cboxLoadedContent']/div/div[2]/div/div[2]/button")
                foodFrst.click()
                confrmOrder = WebDriverWait(self.browser,20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='basket-container']/div[2]/div/div[5]/button")));
                confrmOrder.click()


        
            try:
                payMent = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[8]/div/div/div/div/div[2]/div/div[2]/label/input")));
                payMent.click()
                

            except:
                print("Ödeme yöntemi seçilemedi!")

            talkUS("Ödeme yönteminiz nakit olarak seçildi")
            talkUS("Lütfen siparişinizi onaylayınız")
    
    ymksprs = Yemek(usrnm,pswrd)
    ymksprs.yemekLogin()


def mail_snd():
    talkUS("Hesabınız açılıyor.")
    p_mail = Popen("thunderbird")

def change_bckgrnd():
    
    lst = ["Beijling_park_burial_path_by_Mattias_Andersson.jpg","Ermine_lines_by_Gustavo_Brenner.png","Flight_dive_by_Nicolas_Silva.png","Frozen_sunset_on_the_lake_by_Manuel_Arslanyan.jpg",
"Origin_of_nature_by_Julian_Tomasini.jpg","Sky_Sparkles_by_Joe_Thompson.jpg","Stargazing_by_Marcel_Kächele.jpg","warty-final-ubuntu.png",
"Ubuntu_gel_by_Midge_Mantissa_Sinnaeve.jpg"] 

    talkUS("Arka plan görüntüsünü değiştiriyorum")
    picture_path = "//usr//share//backgrounds//" + random.choice(lst)
    Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format(picture_path), shell=True) 
    

def cpy_text():
    talkUS("Lütfen kopyalamak istediğiniz kelime veya cümleyi söyleyiniz")
    cpy_ans = myCommand()
    
    pyperclip.copy(cpy_ans)  
    talkUS("Google da aramamı ister misiniz?")
    cpy_ans2 = myCommand()
    cpy_yes = ["evet isterim","ara","google ile ara","google'da ara","evet ara","ara ara","evet evet","evet"]
    cpy_no = ["hayır istemiyorum","arama","arama yapma","hayır arama","arama arama","hayır hayır","hayır","google ile arama"]

    if cpy_ans2 in cpy_yes:
        talkUS("Arıyorum")
        outputList = []
        searchOnGoogle(cpy_ans,outputList)
        for output in search(cpy_ans,tld = "co.in",lang = "tr", num = 5, stop = 3 , pause = 2): 
            print(output)
            outputList.append(output) 
        talkUS("İlgili web sayfası açılıyor")
        webbrowser.open(outputList[1])

    if cpy_ans2 in cpy_no:
        talkUS("Tamam söylediğiniz kelime kopyalandı")

def paste_text():
    spam = pyperclip.paste()
    file1 = open("NoteFile.txt","a") 
    file1.write("\n " + spam) 
    file1.close()
    talkUS("Lütfen not dosyasını kontrol ediniz")

def music_spotify():
    sp_username = "" 
    sp_password = "" 
    class Spotify:
        def __init__(self,username,password):
            self.sp_username = sp_username
            self.sp_password = sp_password
            driver = "/home/can/Downloads/chromedriver"
            self.browser = webdriver.Chrome(driver)

        def playMusic(self):
            self.browser.get("https://www.spotify.com/tr/")
            self.browser.maximize_window()

            try:
                firstClick = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/header/div/nav/ul/li[6]/a")));
                firstClick.click()
            except:
                print("Oturum aç tıklanılamadı!")
            
            try:
                secondClick = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/body/div[1]/div[2]/div/div[2]/div/a")));
                secondClick.click()
            except:
                print("Facebook ile oturum açılamadı!")
            
            try:
                fcbkName = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.ID, "email")))
                fcbkPass = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.ID, "pass")))
                fcbkName.send_keys(self.sp_username)
                fcbkPass.send_keys(self.sp_password)
            except:
                print("Kullanıcı bilgileri girilemedi!")
            
            try:
                lgnButton = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.ID, "loginbutton")));
                lgnButton.click()
            except:
                print("Login butonuna tıklanılamadı!")

            try:
                webMusic = WebDriverWait(self.browser,15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/footer/nav/div[2]/dl[3]/dd[2]/a")));
                webMusic.click()
            except:
                print("Web çalar tıklanılamadı!")
            
            time.sleep(7)
            x,y = 998, 1019
            
            try:
                pyautogui.click(x,y)
            except:
                print("Hata!")
    sptfy = Spotify(sp_username,sp_password)
    sptfy.playMusic()




