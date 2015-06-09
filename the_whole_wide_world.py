from flask import Flask, request
import random
import requests
import ipdb
import pickle
from bs4 import BeautifulSoup
app = Flask(__name__)


# Using requests.get() to reterive a url.
#============================================
@app.route('/', methods=['GET'])
def get_datafile():
    # use requests.get(some-url)
    # when page is loaded, this command runs and gets the data and passes it into data
    agent  = 'DataProducts/1.1 (http://galvanize.com; '
    agent += 'class@galvanize.com)'
    headers = {'user_agent': agent}
    url = 'https://www.google.com/search?q=fox+news+anchors&newwindow='
    url += '1&es_sm=119&source=lnms&tbm=isch&sa=X&ei=Box2VebFFcXFogSO6YKoAw&ved=0CAcQ_AUoAQ&biw=1280&bih=641#newwindow=1&tbm=isch&q=female+fox+news+reporters'

    # Wrap in a try-except to prevent a connection error from erroring
    # out the program. Return None if there are any issues.
    try:
        r = requests.get(url, headers=headers)
    except:
        return None

    # Just in case there was a normal error returned. Pass back None.
    if r.status_code != 200: return None

    soup = BeautifulSoup(r.text)

    image_bin = []
    for i in soup.find_all('img'):
        image_bin.append(i.attr['src'])

    return image_bin


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)
