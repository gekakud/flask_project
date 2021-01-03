import os
from flask import Flask, send_from_directory, render_template, abort
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


@app.route("/load_item/<int:index>")
# view function
def load_item_by_index(index):
    try:
        config = db[index]
        return render_template("item_view.html",
                               title="bu ga ga",
                               config=config,
                               index=index,
                               max_index=len(db) - 1)
    except IndexError:
        abort(404, "ERROR 404 - resource not found!")
