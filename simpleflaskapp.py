#################simple Flask web app###########################
from flask import Flask
#creates a wsgi application
app = Flask(__name__)
#helps to define how many urls are there
@app.route("/")
def welcome():
    return "Welcome to the flask Tutrial"
@app.route("/member")
def member():
    return "Welcome to the flask Tutrial of krish naik"

if __name__=="__main__":
    app.run(debug=True)
######################################################################
from flask import Flask
"""It creates an instance of the flask class,
which will be your WSGI(web server gateway interface) application."""
## wsgi application
app = Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to the flask Tutrial"

@app.route("/index")
def to():
    return "Welcome to the flask Tutrial. this should be amazing"

if __name__=="__main__":
    app.run(debug=True)