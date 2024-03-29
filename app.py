import sqlite3
from config import database
from flask import Flask, render_template, send_file
from utils import dates2range

app = Flask(__name__)

"""
Get a connection to the sqlite3 database that can be used to perform SQL
operations.
"""
def get_db_connection():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn

#
# Homepage
#
@app.route('/')
def index():
    # get data from mysql
    conn = get_db_connection()
    projects = conn.execute("SELECT * FROM projects ORDER BY added DESC").fetchall()
    experience_raw = conn.execute("SELECT * FROM experience ORDER BY end_time DESC, start_time DESC").fetchall()
    conn.close()

    # process the experience data to add pretty dates
    # we must make copies since the sqlite3.Row object is not editable
    experience = []
    for e_raw in experience_raw:
        e = dict()
        for k in e_raw.keys():
            e[k] = e_raw[k]
        e['formatted_date'] = dates2range(e_raw['start_time'], e_raw['end_time'])
        experience.append(e)

    # render the page
    return render_template('index.html', projects=projects,
                           experience=experience, title='homepage',
                           fakepath='~')
#
# Public Keys
#
@app.route('/public_keys')
def public_keys():
    return render_template('public_keys.html', title='public_keys')

#
# Resume
#
@app.route('/resume')
def resume():
    return send_file('static/pdf/almondheil-Resume.pdf')

#
# 404 error page
#
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='404',
                           fakepath='/'), 404
