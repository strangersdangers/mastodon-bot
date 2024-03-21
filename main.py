from mastodon import Mastodon
import os
from thingtons import keep_alive

mastodon = Mastodon(
  access_token=os.getenv('TOKEN'),
  api_base_url=os.getenv('INSTURL')
)

mastodon.toot('Toot.')
keep_alive()
