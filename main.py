import sqlite3
from flask import Flask, request

app = Flask(__name__)

from views import *

if __name__ == '__main__':
    app.run(debug=True)