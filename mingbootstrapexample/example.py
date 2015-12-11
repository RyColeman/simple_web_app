from flask import Flask, request, render_template
from bokeh.plotting import figure, output_notebook, show
from bokeh import embed
from bokeh.models import HoverTool

app = Flask(__name__)

def create_linechart():
    x = range(1, 10)
    y = range(1, 10)

    hover = HoverTool(tooltips=[("(x, y)", "($x, $y)")])
    tools = "box_select,lasso_select,help"
    p = figure(plot_width=400, plot_height=400, tools=[hover, tools])

    p.line(x, y)

    return p

# home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    chart = create_linechart()
    script, div = embed.components(chart)
    return render_template('dashboard.html', script=script, div=div)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
