from mastodon import Mastodon
from datetime import datetime
import os
from random import random
from random import randint
import time
import xml.etree.ElementTree as ET
found = False
#Abrimos XML con los datos de textos
tree = ET.parse('./dias/desc_sam.xml')
xmlpath = "./description"
root = tree.getroot()
#Objeto de Mastodon
mastodon = Mastodon(
    access_token = os.environ['KEY'],
    api_base_url = os.environ['INS']
    )
#Seleccionamos día de la semana
files = []
dt = datetime.now()
x = dt.weekday()
#Abrimos carpeta correspondiente al día de la semana
path = "./dias/sam/"
pathfiles = "./dias/memes.txt"
files = os.listdir(path)
num_files = len(files)
#Si encontramos archivos...
if num_files >= 1:
    #Seleccionamos uno al azar
    while found == False:
        position = randint(0, num_files-1)
        file = files[position]
        with open(pathfiles, "r+") as f:
            content = f.read()
            if file not in content:
                found = True
                
    fileappend = open(pathfiles, "a")
    fileappend.write(file)
    fileappend.write("\n")
    fileappend.close()
    #Buscamos su información en el archivo de textos
    path_id = xmlpath + "[@id='" + file + "']"
    for item in root.findall(path_id):
        print(path_id)
        texto = item[0].text #Texto del toot
        desc  = item[1].text #Alt text
    #Concatenamos la ruta completa
    media_path = path + file
    #Anexamos el archivo al objeto media_post de Mastodon
    media = mastodon.media_post(media_path, description=desc)
    #Dejamos que se procese todo trankiliyo sosegado relajao relajao
    time.sleep(30)
    #Tooteamos
    toot = mastodon.status_post(texto, media_ids=media, visibility='unlisted')
