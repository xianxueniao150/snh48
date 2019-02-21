from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zbw1056512354@localhost/micmovie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return render_template('snh/bili.html')

import datetime
@app.route('/tiezi', methods=['GET', 'POST'])
def snh():
    posts = []
    if request.method == 'POST':
        date = request.form.get("date")
        for post in Snh.query.all():
            if post.time.date()==datetime.datetime.strptime(date, '%Y-%m-%d').date():
                posts.append(post)
    return render_template('snh/tieba.html', posts=posts)

class Snh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    creater = db.Column(db.String(255))
    post_url = db.Column(db.String(255))
    time = db.Column(db.DateTime)
    post_lz = db.Column(db.Text)
    reply_num = db.Column(db.Integer)


