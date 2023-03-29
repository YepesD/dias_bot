from mastodon import Mastodon
from datetime import datetime
import os
from random import random
from random import randint
import time
import xml.etree.ElementTree as ET
#Abrimos XML con los datos de textos
tree = ET.parse('./dias/desc.xml')
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
path = "./dias/" + str(x) + "/"
files = os.listdir(path)
num_files = len(files)
#Si encontramos archivos...
if num_files >= 1:
    #Seleccionamos uno al azar
    position = randint(0, num_files-1)
    file = files[position]
    #Buscamos su información en el archivo de textos
    path_id = xmlpath + "[@id='" + file + "']"
    for item in root.findall(path_id):
        texto = item[0].text #Texto del toot
        desc  = item[1].text #Alt text
    #Concatenamos la ruta completa
    media_path = path + file
    for attempt in range(10):
        try:         
            #Anexamos el archivo al objeto media_post de Mastodon
            media = mastodon.media_post(media_path, description=desc)
            #Dejamos que se procese todo trankiliyo sosegado relajao relajao
            time.sleep(30)
        except:
            print("Error en la subida de media, reintentamos")
        else:
            break
    else:
        print("Error en la subida de media")
    for attempt2 in range(10):
        try:
            #Tooteamos
            toot = mastodon.status_post(texto, media_ids=media, visibility='private')
        except:
            print("Error al enviar toot, reintentamos")
    else:
        print("Error al enviar toot")
        
