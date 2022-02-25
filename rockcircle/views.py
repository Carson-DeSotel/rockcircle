from flask import render_template
from rockcircle import app

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home')