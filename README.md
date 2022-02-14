# rockcircle

rockcircle is a LAN app to coordinate the hit game "Saboteur Rock" developed by Brett Braza. 

## Installation:

### Prerequisites:

Please have an installation of Python 3 on your machine. 

### Mangaing a Virtual Environment:
rockcircle must be installed and ran locally. We use Python's venv virtual environment control system to manage package dependencies across systems.

```
pip install -e .
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
python -m pip install -r requirements.txt
```

To exit the virtual environment, simply run ```deactivate```.

## Running the Server:

We're using gunicorn to handle running the server. It can be executed from inside the venv environment in the base directory using the command

```
gunicorn --bind localhost:42069 rockcircle.wsgi:app
```

## References:
[1] https://docs.python.org/3/tutorial/venv.html  
[2] https://flask.palletsprojects.com/en/2.0.x/quickstart/  
[3] https://flask.palletsprojects.com/en/2.0.x/installation/  
[4] https://github.com/pallets/flask/tree/2.0.2/examples/tutorial  
[5] https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04  
[6] https://www.python-boilerplate.com/py3+flask+gitignore+logging+unittest  