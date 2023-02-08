from mastodon import Mastodon
import time
import os

#Ejecución especial de viernes noche
#Creamos objeto Mastodon
mastodon = Mastodon(
    access_token = os.environ['KEY'],
    api_base_url = 'https://owo.cafe'
    )
#El toot va hardcodeado. Siempre es el mismo
texto = "There's always time for fun... It's Friday night"

path = "./dias/night/Fridaynight.mp4"
desc = "Videojuego Killer7. Kun Lan habla con Harman Smith"
media = mastodon.media_post(path, description=desc)
time.sleep(30)
toot = mastodon.status_post(texto, media_ids=media)
