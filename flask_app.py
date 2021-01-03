import os
from flask import Flask, send_from_directory, render_template, abort
from dummy_db import db
from mongo_db import mongo_client
import common as cmn

# ctor - creates global flask app
app = Flask(__name__)

# decorates show_main_view func
@app.route("/")
# view function
def show_main_view():

    return render_template("main_view.html",
                           title=cmn.main_view_page_title,
                           num_of_items=mongo_client.configs_count(),
                           items=db)


@app.route("/load_item/<int:index>")
# view function
def load_item_by_index(index):
    try:
        config = db[index]
        return render_template("item_view.html",
                               title=str(cmn.item_view_page_title + str(index)),
                               config=config,
                               index=index,
                               max_index=len(db) - 1)
    except IndexError:
        abort(404, cmn.not_found_error_message)


# TODO: fix this to load webpage icon
@app.route('/favicon.ico')
def show_favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')
