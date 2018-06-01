from flask import Flask, render_template
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")

    db = SQLAlchemy(app)

    class Page(db.Model):
        __tablename__ = 'page'
        id = Column(Integer, primary_key=True)
        title = Column(String)
        content = Column(String)

    db.create_all()

    @app.route('/')
    def index():
        page = Page.query.filter_by(id=1).first()

        return render_template("index.html", TITLE=page.title, CONTENT=page.content)

    @app.route('/about')
    def about():
        con = psycopg2.connect("dbname=pythonthusiast_flask user=devuser password=devpassword host=postgres")
        cur = con.cursor()

        cur.execute("select * from page;")
        id, title, content = cur.fetchone()

        con.close()

        return render_template("about.html", TITLE=title)

    return app
