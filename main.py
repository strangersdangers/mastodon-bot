from mastodon import Mastodon
import os
from thingtons import keep_alive

mastodon = Mastodon(api_base_url = os.getenv('INSTURL'), access_token = os.getenv('TOKEN'))

#mastodon.toot('Working!!')
mastodon.media_post("https://images.dog.ceo/breeds/cattledog-australian/IMG_5177.jpg", "image/jpeg")
keep_alive()
