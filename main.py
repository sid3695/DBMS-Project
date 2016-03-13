from flask import Flask, render_template, request, redirect, url_for
import pickle
import datetime
from utils import *

###########BLUEPRINTS#############
from views.students import sapp
from views.courses import capp
from views.relations import rapp
from views.co_allocs import papp


app = Flask(__name__)
app.register_blueprint(sapp)
app.register_blueprint(capp)
app.register_blueprint(rapp)
app.register_blueprint(papp)
##################################

app.config['DEBUG'] = True
app.secret_key = 'e\x9e#lW+\xcad\xbd\xd9y^\y15\y86\x9d\xaf\xce\x9aP\xe8g%\xc5d'



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)