from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

from views import *

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
