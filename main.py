from mastodon import Mastodon
import os
#from thingtons import keep_alive
from flask import Flask, request
import requests

app = Flask(__name__)
mastodon = Mastodon(api_base_url = os.getenv('INSTURL'), access_token = os.getenv('TOKEN'))

@app.route('/')
def home():
  return "<h1>" + "Website proudly hosted by cyclic!" + "</h1>"
  #end
@app.route('/post')
def post():
  type = request.args.get('type')
  quote = []
  data = []
  randomquote = []
  dogurl = []
  imagetoget = []
  data2 = []
  if type == 'text':
    randomquote = requests.get("https://api.quotable.io/quotes/random")
    data = randomquote.json()
    quote = f"woke up from my break just to post this. heres a quote for yall: {data['content']} -{data['author']}"
    mastodon.toot(quote)
    return 'posted text'
    if type == 'img':
      dogurl = requests.get("https://dog.ceo/api/breeds/image/random")
      data2 = dogurl.json()
      imagetoget = requests.get(data2['message']).content
      mastodon.media_post(imagetoget, 'image/jpg')
      return 'posted img'
    else:
      return make_response("yo wassup you just hit the hood")
      #end.. or is it?
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
