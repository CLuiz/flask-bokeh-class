from flask import Flask, render_template
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import INLINE
import sqlite3
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'


# add data from db
def get_data():
    with sqlite3.connect('greenhouse.db') as connection:
        c = connection.cursor()
        c.execute('SELECT * FROM greenhouse')
        data = c.fetchall()
    return data

@app.route('/chart')
def chart():
    # create chart
    p = figure(plot_width=1000, plot_height=400, x_axis_type='datetime')

    # add line renderer
    data = get_data()
    p.line([datetime.datetime.fromtimestamp(d[0]) for d in data], [d[1] for d in data], line_width=2)

    # grab static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # generate javascript and the actual chart components
    script, div = components(p)

    # render template
    return render_template(
    'chart.html',
    plot_script=script,
    plot_div=div,
    js_resources=js_resources,
    css_resources =css_resources,
    )

if __name__ == '__main__':
    app.run(debug=True)
