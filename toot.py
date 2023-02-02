from mastodon import Mastodon
from datetime import datetime
from os import listdir
import os
from random import random
from random import randint
import time
import config

mastodon = Mastodon(
    access_token = os.environ['KEY'],
    api_base_url = 'https://owo.cafe'
    )
files = []
dias = ["Es lunes", "Es martes", "Es miércoles", "Es jueves", "Es viernes!!!!", "Es sábado", "Es domingo"]
dt = datetime.now()
x = dt.weekday()

path = "./dias/" + str(x) + "/"
files = os.listdir(path)
texto = dias[x]
num_files = len(files)
if num_files >= 1:
    position = randint(0, num_files-1)
    file = files[position]

    media_path = path + file

    media = mastodon.media_post(media_path)
    time.sleep(10)
    toot = mastodon.status_post(texto, media_ids=media)
