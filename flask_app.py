import os
from flask import Flask, send_from_directory, render_template, abort
from mongo_db import mongo_client
import common as cmn
# from dummy_db import db

# ctor - creates global flask app
app = Flask(__name__)


# decorates show_main_view func
@app.route("/")
# view function
def show_main_view():

    return render_template("main_view.html",
                           title=cmn.main_view_page_title,
                           num_of_items=mongo_client.configs_count(),
                           configs=mongo_client.get_all_configs())


@app.route("/load_item/<string:key>")
# view function
def load_item_by_index(key):
    try:
        config = mongo_client.get_config_by_key(key)
        return render_template("item_view.html",
                               title=str(cmn.item_view_page_title + key),
                               config=config,
                               key=key)
    except IndexError:
        abort(404, cmn.not_found_error_message)


# TODO: fix this to load webpage icon
@app.route('/favicon.ico')
def show_favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')
