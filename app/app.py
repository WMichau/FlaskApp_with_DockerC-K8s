from crypt import methods
from flask import Flask, jsonify, render_template, url_for, redirect, request
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'knights'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)




@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":    
        if request.form['submit_button'] == 'Get from DB':
            conx = mysql.connect()

            cursor = conx.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM favorite_colors")

            rows = cursor.fetchall()
            
            return render_template("index.html", rows=rows)
    return render_template("index.html")        

# @app.route('/get_data')
# def db():
#     conx = mysql.connect()

#     cursor = conx.cursor(pymysql.cursors.DictCursor)
#     cursor.execute("SELECT * FROM favorite_colors")

#     rows = cursor.fetchall()

#     print(type(rows))

#     return redirect(url_for('main', rows=rows))



    # resp = jsonify(rows)
    # resp.status_code = 200

    # return resp
@app.route('/insert_data', methods=['POST'])
def idb():
    if request.method == 'POST':

        n = request.form['name']
        c = request.form['color']
        
        conx = mysql.connect()

        cursor = conx.cursor(pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO favorite_colors (name, color) VALUES (%s, %s)", (n, c))
        conx.commit()

    return redirect(url_for("main"))

if __name__ == '__main__':
    app.run()
