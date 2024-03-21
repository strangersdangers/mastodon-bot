from mastodon import Mastodon
import os
from thingtons import keep_alive

mastodon = Mastodon(access_token = os.getenv('TOKEN'))

mastodon.toot('Toot.')
keep_alive()
