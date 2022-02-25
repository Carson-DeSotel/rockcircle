# rockcircle

rockcircle is a LAN app to coordinate the hit game "Saboteur Rock" developed by Brett Braza. 

## Installation:

### Prerequisites:

Please have an installation of Python 3, flask, and pip on your machine.

### Mangaing a Virtual Environment:
rockcircle must be installed and ran locally. We use Python's venv virtual environment control system to manage package dependencies across systems.

First, create a virtual environment (from the root directory)
```bash
python3 -m venv ./venv
```
The virtual environment should be activated before installing on Windows / *NIX systems.

On Windows:
```
> venv\Scripts\activate
```

On Mac / Linux:
```
$ . venv/bin/activate
```

From there, install the necessary requirements from the requirements.txt file by running 

```
python3 -m pip install -r requirements.txt
```

To exit the virtual environment, simply run ```deactivate```.

## Running the Server:

We're running the server natively with flask. Make sure the environment is activated, then run 

```bash
flask run
```

## Organization
The basis for organization is based on several articles online. 

Note: some folders will have a .default.extension file so that we can commit the hierarchy to GitHub. These may be deleted once each folder is initialized.

```
rockcircle/         -- project root
|_ rockcircle/      -- module root
  |_ lib            -- library files for module (logic, classes, functions, etc.)
  |_ static         -- files for web design & client
    |_ css          -- css files
    |_ js           -- javascript files
  |_ templates      -- Jinja2 template / HTML files
  |_ __init__.py    -- module initialization, handles importing & app setup
  |_ handles.py     -- WebSocketIO Handles for Server / Client Integration
  |_ views.py       -- handle making pages
|_ venv/            -- handle virtual environment locally
|_ .flaskenv        -- Flask environment variables (should be OS independent)
|_ .gitignore     
|_ config.py        -- Additional App configurations
|_ README.md
|_ requirements.txt -- packages to install for venv
|_ rockcircle.py    -- main app file
|_ setup.py         -- setup module
```

## References:
[1] https://docs.python.org/3/tutorial/venv.html  
[2] https://flask.palletsprojects.com/en/2.0.x/quickstart/  
[3] https://flask.palletsprojects.com/en/2.0.x/installation/  
[4] https://github.com/pallets/flask/tree/2.0.2/examples/tutorial  
[5] https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04  
[6] https://www.python-boilerplate.com/py3+flask+gitignore+logging+unittest  
[7] https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
[8] https://github.com/miguelgrinberg/Flask-SocketIO/blob/main/example/app.py  