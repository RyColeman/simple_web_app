import pdb
import json
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/add", methods=['POST'])
def add():
	pdb.set_trace()

	if request.method == 'POST':
		data = {
	    	'input'  : request.form,
			'output' : int(request.form['first']) + int(request.form['second'])
			}
		js = json.dumps(data)
		return Response(js, status=200, mimetype='application/json')
	else:
		return "POST NUMBERBERSBERS!!!"

# Order of routes matters
@app.route("/<name>")
def hello(name):
    return "Hello " + name + "!\nWelcome to slow-awkward-calculator :)"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

