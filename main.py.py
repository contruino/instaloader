import eel
import instaloader
from pathlib import Path

eel.init("web")

@eel.expose
def recv_data(nick):
    print(nick)
    try:
        ig = instaloader.Instaloader()
        ig.download_profile(nick, profile_pic_only=False)
    except  Exception  as x :
        print(x)

eel.start("index.html",size=(500,500), port=8080) 