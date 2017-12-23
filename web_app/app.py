from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template("index.html")


    @app.route('/about')
    def about():
        return 'About me'

    return app