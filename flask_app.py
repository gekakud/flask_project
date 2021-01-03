import os
from flask import Flask, send_from_directory, render_template
from dummy_db import db

# ctor - creates global flask app
app = Flask(__name__)


# decorates show_main_view func
@app.route("/")
# view function
def show_main_view():
    return render_template("main_view.html",
                           message="some temp message",
                           title="bu ga ga",
                           config="")


# TODO: fix this to load webpage icon
@app.route('/favicon.ico')
def show_favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@app.route("/load_items")
# view function
def load_all_items():
    config = db[0]
    return render_template("main_view.html",
                           message="some temp message",
                           title="bu ga ga",
                           config=config)
