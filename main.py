from mastodon import Mastodon
import os
#from thingtons import keep_alive
from flask import Flask, request
import requests

app = Flask(__name__)
mastodon = Mastodon(api_base_url = os.getenv('INSTURL'), access_token = os.getenv('TOKEN'))

@app.route('/')
def home():
  testing = mastodon.account_verify_credentials().acct
  return "<h1>" + "Website proudly hosted by cyclic!" + "</h1>"
  print(f"ATTENTION, PLEASE VIEW TESTING: {testing}")
  #end
@app.route('/post')
def post():
  type = request.args.get('type')
  auth = request.args.get('pass')
  quote = []
  data = []
  randomquote = []
  dogurl = []
  imagetoget = []
  image = []
  thekey = os.getenv('PASS')
  id = []
  data2 = []
  if auth is None:
    return "one parameter missing: auth", 403
  if auth != thekey:
    return "auth failed, womp womp", 403
  else:
    if type == 'text':
      randomquote = requests.get("https://api.quotable.io/quotes/random")
      data = randomquote.json()
      quote = f"woke up from my break just to post this. heres a quote for yall: {data[0]['content']} -{data[0]['author']}"
      mastodon.toot(quote)
      return 'posted text'
    elif type == 'img':
      dogurl = requests.get("https://dog.ceo/api/breeds/image/random")
      data2 = dogurl.json()
      imagetoget = requests.get(data2["message"])
      image = imagetoget.content
      print(data2)
      id = mastodon.media_post(image, 'image/png').id
      mastodon.status_post("New dog picture for you!", media_ids=id)
      return 'posted img'
    elif type is None:
      return "yooo"
      #end.. or is it?
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000) #use waitress-serve or uvicorn for production
