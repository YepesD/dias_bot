from mastodon import Mastodon
import time
import config

mastodon = Mastodon(
    access_token = config.access_token,
    api_base_url = 'https://owo.cafe'
    )

texto = "There's always time for fun... It's Friday night"

path = "./dias/night/Fridaynight.mp4"

media = mastodon.media_post(path)
time.sleep(10)
toot = mastodon.status_post(texto, media_ids=media)
