from rockcircle.wsgi import app

@app.route('/')
def index():
    return 'Hello World!'