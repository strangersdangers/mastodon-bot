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
  image = []
  data2 = []
  test = []
  if type == 'text':
    randomquote = requests.get("https://api.quotable.io/quotes/random")
    data = randomquote.json()
    quote = f"woke up from my break just to post this. heres a quote for yall: {data[0]['content']} -{data[0]['author']}"
    test = mastodon.toot(quote).url
    return 'posted text'
    print(test)
  elif type == 'img':
    dogurl = requests.get("https://dog.ceo/api/breeds/image/random")
    data2 = dogurl.json()
    imagetoget = requests.get(data2["message"])
    image = imagetoget.content
    print(data2)
    mastodon.media_post('Bgforanything.png', 'image/png')
    return 'posted img'
  elif type is None:
    return "yooo"
    #end.. or is it?
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
