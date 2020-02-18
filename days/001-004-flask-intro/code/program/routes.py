from flask import render_template
from program import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    # Extra params for return render_template: title = 'Template Demo', time = timenow
    # Extra params didn't work when I tried them
    # TODO: understand what extra params do & how to make them work


@app.route('/100Days')
def p100days():
    return render_template('100Days.html')





