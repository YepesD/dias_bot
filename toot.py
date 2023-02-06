from mastodon import Mastodon
from datetime import datetime
import os
from random import random
from random import randint
import time
import xml.etree.ElementTree as ET

tree = ET.parse('./dias/desc.xml')
path = "./description"
root = tree.getroot()

mastodon = Mastodon(
    access_token = os.environ['KEY'],
    api_base_url = 'https://owo.cafe'
    )
files = []
dt = datetime.now()
x = dt.weekday()

path = "./dias/" + str(x) + "/"
files = os.listdir(path)
texto = dias[x]
num_files = len(files)
if num_files >= 1:
    position = randint(0, num_files-1)
    file = files[position]
    path_id = path + "[@id='" + file + "']"
    for item in root.findall(path_id):
        texto = item[0].text
        desc  = item[1].text
    media_path = path + file
    media = mastodon.media_post(media_path, description=desc)
    time.sleep(30)
    toot = mastodon.status_post(texto, media_ids=media)
