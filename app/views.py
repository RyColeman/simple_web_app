from app import app
from flask import render_template, Flask, request, Response
import ipdb
import json

@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"

@app.route("/add", methods=['POST'])
def add():
    ipdb.set_trace()

    if request.method == 'POST':
        data = {
            'input'  : request.form,
            'output' : int(request.form['first']) + int(request.form['second'])
            }
        js = json.dumps(data)
        rs = Response(js, status=200, mimetype='application/json')
        ipdb.set_trace()
        return rs
    else:
        return "POST NUMBERBERSBERS!!!"

# Order of routes matters
@app.route("/<name>")
def hello(name):
    return "Hello " + name + "!\nWelcome to slow-awkward-calculator :)"






@app.route('/user')
def user():
    user = { 'nickname': 'Oren' } # fake user
    simple_html = '''
        <html>
          <head>
            <title>Home Page</title>
          </head>
          <body>
            <h1>Hello, ''' + user['nickname'] + '''</h1>
          </body>
        </html>
        '''
    return simple_html   


@app.route('/user2')
def user2():
    user = { 'nickname': 'Orener' }
    return render_template("user.html",
        title = 'Home',
        user = user)     




@app.route('/predict', methods=['POST'])
def predict():
    article = request.form['article']    


