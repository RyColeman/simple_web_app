from flask import Flask
from flask import request, make_response
import json
import StringIO

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
app = Flask(__name__)


# Form page to submit text
#============================================
# create page with a form on it
@app.route('/')
def submission_page():
    return '''
    <form action="/word_counter" method='POST' >
        <input type="text" name="user_input" />
        <input type="submit" />
    </form>
    '''


# My word counter app
#==============================================
# create the page the form goes to
@app.route('/word_counter', methods=['POST', 'GET'] )
def word_counter():
    if request.method=='GET':
        return '''
        <form action="/word_counter" method='POST' >
        <input type="text" name="user_input" />
        <input type="submit" />
        </form>
        '''
    # get data from request form, the key is the name you set in your form
    data = request.form['user_input']

    # convert data from unicode to string
    #data = str(data)

    # run a simple program that counts all the words
    dict_counter = {}
    for word in data.lower().split():
        if word not in dict_counter:
            dict_counter[word] = 1
        else:
            dict_counter[word] += 1
    total_words = len(dict_counter)

    # now return your results
    return json.dumps(dict_counter)
    return 'Total unique words is %i, <br> dict_counter is: %s' % (total_words, dict_counter)

@app.route('/pretty-pictures')
def get_graph():
    import pandas as pd
    import numpy.random as nrandom
    df = pd.DataFrame({'x':range(10),
                       'y':nrandom.rand(10)})

    df = df.set_index('x')
    output = StringIO.StringIO()

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    df.y.plot(ax=axis)
    
    canvas = FigureCanvas(fig)

    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response
    
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
