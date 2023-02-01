from flask import Flask

app = Flask(__name__, static_folder='public')

from app.controllers.index import index 
