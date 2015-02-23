
# Using HTML templates.  
**Python + HTML = Jinja2**  
A Jinja2 template is an some.html page that can speak both python and html.
To get started  `easy_install Jinja2` or `pip install Jinja2`

This is how you have to setup your files when using html templates with flask.
```
MyProject/
|-- my_app/
|   |-- app.py
|   |-- templates/
|   |   |-- index.html
|   |-- static/
|   |   |-- mycss.css
|   |   |-- image.png
```
Here is an example of how to setup your app.py file if you want to work with an html template file.  

*MyProject/my_app/**app.py***
```python
#MyProject/my_app/app.py
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969, debug=True)
```





# How to build a text classifier web app.  
Today we are going to train a model, build a web interface that allows people to submit data, send that data to our model, make a prediction on it, then return the results.  

# Step 1: Build and save your model.  
1. Import pickle and use it to load the articles.pkl file.
https://wiki.python.org/moin/UsingPickle

2. Set your text data column to `X`.

3. Set your label data column to `y`.

2. Initialize a multinomial naive bayes classifier.  

3. Initialize a TFIDF vectorizer.

4. With your TFIDF vectorizer, fit and transform your `X` text data. Name the output `vectorized_X`
.
5.  Initialize your MultinomialNB model
```clf = MultinomialNB()```

6.  Fit your model with the `transformed_X` data, and the `y` labels.  

7.  Export your fitted model using pickle.

8.  Export your fitted vectorizer using pickle.

9.  Take a mini break.
---
<br>
<br>
<br>
