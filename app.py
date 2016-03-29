from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Pastechi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.String(80), unique=True)
    price = db.Column(db.String(120) )
    stock = db.Column(db.INT(120), default=0)


    def __init__(self, flavor, price):
        self.username = flavor
        self.email = price

    def __repr__(self):
        return '<Pastechi %r>' % self.username


@app.route("/")
def home_base():
    return render_template('front.html')


@app.route("/pastechis")
def pastechi_list():
    return render_template('base.html')


@app.route("/pastechi/:pastechi_id")
def single_pastechi(pastechi_id):
    return render_template('base.html')


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(debug=True)
