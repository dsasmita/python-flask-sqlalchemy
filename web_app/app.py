from flask import Flask, render_template
import psycopg2

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")

    @app.route('/')
    def index():
        con = psycopg2.connect("dbname=pythonthusiast_flask user=devuser password=devpassword host=postgres")
        cur = con.cursor()

        cur.execute("select * from page where id = 1;")
        id, title = cur.fetchone()

        con.close()

        return render_template("index.html", TITLE = title)


    @app.route('/about')
    def about():
        con = psycopg2.connect("dbname=pythonthusiast_flask user=devuser password=devpassword host=postgres")
        cur = con.cursor()

        cur.execute("select * from page where id = 2;")
        id, title = cur.fetchone()

        con.close()

        return render_template("about.html", TITLE = title)


    return app