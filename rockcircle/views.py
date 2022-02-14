from flask import (render_template)
from rockcircle import app

@app.route('/', methods=['GET', 'POST'])
def index():
    users_fnames = ['Carson', 'Zach', 'Jeremy']
    users = []
    
    for user in users_fnames:
        users.append({'username':user})

    return render_template('index.html', title='Home', users=users)