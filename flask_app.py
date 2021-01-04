import os
from flask import Flask, send_from_directory, render_template, abort, request, redirect, url_for
from mongo_db import mongo_client
import common as cmn

# ctor - creates global flask app
app = Flask(__name__)


# decorates show_main_view func
@app.route("/", methods=["GET", "POST"])
# view function
def show_main_view():
    if request.method == "POST":
        print("POST new config")
        new_config = {'key': request.form['config_name'], 'value': request.form['config_value']}
        mongo_client.insert_new_config(new_config)
        return redirect(url_for("show_main_view"))
    else:
        print("GET all")
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


@app.route("/add_config", methods=["GET", "POST"])
def add_new_config():
    print("in add_new_config")
    if request.method == "POST":
        print("post detected")
        new_config = {'key': request.form['config_name'], 'value': request.form['config_value']}
        mongo_client.insert_new_config(new_config)
        return redirect(url_for("show_main_view"))
    else:
        return render_template("add_config.html",
                               title=cmn.add_new_config_page_title)


@app.route('/edit_config/<string:key>')
def edit_config(key):
    return render_template("edit_config_view.html",
                           title=str(key),
                           key=key)


@app.route('/delete_config/<string:key>')
def delete_config(key):
    mongo_client.delete_config(key)
    return redirect(url_for("show_main_view"))
