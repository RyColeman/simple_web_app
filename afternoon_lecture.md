
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


