from flask import Flask, request, render_template

app = Flask(__name__)

# home page
@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Page Title</title>
            </head>
          <body>
            <!-- page content -->
            <h1>My Page</h1>
            <p>
                All the things I want to say.
            </p>
            <a href="/page2">Page 2<a>
          </body>
        </html>
        '''

@app.route('/page2')
def page2():
    x = range(1, 101)
    y = range(2, 102)
    data = zip(x, y)
    return render_template('table.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
