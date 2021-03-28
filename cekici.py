import json
import time
import datetime
import requests
from PIL import Image, ImageDraw, ImageFont


def createProfilePhoto(time: str, backgroundColor: tuple, textColor: tuple) -> str:
    img = Image.new('RGB', (1000, 1000), color = backgroundColor) # background color
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 200)
    d.text((200, 400), time, fill= textColor, font=font) # text
    
    img.save("profilePhoto.png")

    return r"profilePhoto.png"


def gTime() -> str:
    time = datetime.datetime.now()
    print(time.hour, ":", time.minute)

    return str(time.hour) + " : " + str(time.minute)


def createSession(username: str, password: str):
    uri = "https://instagram.com"

    with requests.session() as session:
        session.headers = {"User-Agent":"Mozilla/5.0"}

        session.get(uri)
        session.headers.update(
				{'X-CSRFToken': session.cookies['csrftoken']}
			)

        loginData = {
            "username":username,
            "enc_password":"#PWD_INSTAGRAM_BROWSER:0:0:"+password,
            "queryParams": '{}'
        }

        r = session.post(uri+"/accounts/login/ajax/", data=loginData)

        session.headers.update({'X-CSRFToken': session.cookies['csrftoken']})
        
        auth = r.json()

        if 'authenticated' in auth:
            if auth['authenticated']:
                
                return session
            else:
                return "[ ! ] Şifre yanlış"
        else:
            return "[ ! ] Bir şeyler yanlış gitti"


def changePp(session, file):
    uri = "https://instagram.com"
    with open(file, "rb") as saatResim:

        a = session.post(uri+"/accounts/web_change_profile_picture/", files= {
            'profile_pic': ('pp.jpg', saatResim.read(), 'image/jpeg')})

        session.headers.update({'X-CSRFToken': session.cookies['csrftoken']})

        return session


def worker():
    config = open("config.json", "r", encoding="utf-8")
    config = json.load(config)

    username = config['username']
    password = config['password']
    backgroundColor = config["background_color"]
    textColor = config["text_color"]
    delay = config["delay"]

    temp = None
    SESSION = createSession(username, password)

    if not "[ ! ]" in str(SESSION):
        while True:
            timeNow = gTime()

            if temp != timeNow:
                pphoto = createProfilePhoto(timeNow, tuple(backgroundColor), tuple(textColor))
                resp = changePp(SESSION, pphoto)

                if not "[ ! ]" in str(resp):
                    SESSION = resp
                else:
                    print(resp)

                temp = timeNow
            
            time.sleep(delay)
    else:
        print(SESSION)


worker()