from flask import Flask, request, render_template

app = Flask(__name__)

'''
    Global Variables:
'''
GUEST_LIST = []

'''
    Pages:
'''
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_guest', methods=['GET', 'POST'])
def add_guest():
    if request.method == 'POST':
        GUEST_LIST.append(request.form.get('fname'))
    print(GUEST_LIST)

    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=42069)