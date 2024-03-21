from mastodon import Mastodon
import os
from thingtons import keep_alive

mastodon = Mastodon(api_base_url = os.getenv('INSTURL'), access_token = os.getenv('TOKEN'))

mastodon.toot('Toot.')
keep_alive()
