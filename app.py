import os
import sqlite3
from flask import Flask, request, g
app = Flask(__name__)

DATABASE = 'global.db'

# helper method, allows database access within a controller


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# create our database structure, which is akin to a dict with one key
def init_db():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS store
                (id INTEGER PRIMARY KEY, image BLOB)''')
    cur.execute("INSERT OR IGNORE INTO store (id, image) VALUES (1, '')")
    db.commit()
    db.close()


# initialize db for every app instance
init_db()


# recieve images and write to db as BLOB if the password query is correct
@app.route('/', methods=['POST'])
def update_image():
    db = get_db()
    cur = db.cursor()
    if request.args.get('password') != os.environ['PASSWORD']:
        return '', 400
    else:
        image = [request.data]
        cur.execute(
            "UPDATE store SET image=? WHERE id=1", image)
        db.commit()
        return '', 200


# share images naively and let browsers interpret the blob as jpeg
@app.route('/live.jpeg')
def get_image():
    cur = get_db().cursor()
    image = cur.execute("SELECT image FROM store WHERE id=1").fetchone()[0]
    return image, 200


# test route that mimics having a live cam
@app.route('/test')
def test_image():
    return '''<img src="/live.jpeg" /><script>setInterval(() =>
        document.querySelector(\'img\').src = \'/live.jpeg?\' + Date.now(), 150)</script>'''


# close the database connection after every request ends
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
