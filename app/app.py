from flask import Flask, jsonify, render_template
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'knights'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)




@app.route('/')
def main():
    return render_template("index.html")

@app.route('/db')
def db():
    conx = mysql.connect()

    cursor = conx.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM favorite_colors")

    rows = cursor.fetchall()

    resp = jsonify(rows)
    resp.status_code = 200

    return resp

if __name__ == '__main__':
    app.run()
