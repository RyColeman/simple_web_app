from flask import Flask, request
from collections import Counter
import pickle
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from build_model_py3 import TextClassifier

# Initializing app
app = Flask(__name__)

with open('data/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('data/X.pkl', 'rb') as f:
    X = pickle.load(f)

with open('data/y.pkl', 'rb') as f:
    y = pickle.load(f)

model.fit(X, y)

@app.route('/')
def index():
    return '''
    <form action="/submit" method='GET'>
        <input type="submit" value = 'Hey thilly gooose, wanna see what type of article your writing most likely is? Click here to find out, ya big thillly :-)' />
    </form>
    '''

@app.route('/submit')
def submit():
    return '''
    <form action="/predict" method='POST'>
        <input type="text" name="user_input" />
        <input type="submit" value = 'Hey there thuper thilly, type in some words and see what type of article it most likely is, ya big ol THILLY GooooSe!' />
    </form>
    '''

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    text = np.array([str(request.form['user_input'])])
    prediction = model.predict(text)
    output = "Here's what your writing resembles : {}".format(prediction)
    go_back_to_submit = '''
    <form action="/submit">
        <input type="submit" value="Make thome more writings ya Big OL GOOOOOSE!" />
    </form>
    '''

    return output + go_back_to_submit


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
