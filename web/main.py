from flask import Flask
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI


@app.route('/')
def index():
    return 'Flask app'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
