from flask import Flask, send_from_directory, render_template, abort, request, redirect, url_for
from mongo_db import mongo_client
import common as cmn

# ctor - creates global flask app
app = Flask(__name__)


def generate_text_from_configs(all_configs):
    text = ""
    for config in all_configs:
        line = "#define " + config['key'] + " " + config['value']
        text = text + line + "\n"
    return text


# decorates show_main_view func
@app.route("/", methods=["GET", "POST"])
# view function
def show_main_view():
    try:
        if request.method == "POST":
            print("POST new config")

            new_config = {'key': request.form['config_name'], 'value': request.form['config_value']}
            mongo_client.insert_new_config(new_config)
            return redirect(url_for("show_main_view"))
        else:
            print("GET all")
            all_configs = mongo_client.get_all_configs()
            gen_text = generate_text_from_configs(mongo_client.get_all_configs())
            print(gen_text)
            return render_template("main_view.html",
                                   title=cmn.main_view_page_title,
                                   configs=all_configs,
                                   generated_text=gen_text)
    except Exception:
        print("show_main_view failed")


@app.route("/load_item/<string:key>")
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


@app.route('/edit_config/', methods=["GET", "POST"])
def edit_config():
    key = request.form['hidden_key']
    value = request.form['new_config_value']
    print("edit config key:" + key)
    print("edit config value:" + value)
    mongo_client.update_config_value({'key': key, 'value': value})
    return redirect(url_for("show_main_view"))


@app.route('/delete_config/')
def delete_config():
    key = request.args.get('key', default=None, type=str)
    print("delete config with key:" + key)
    mongo_client.delete_config(key)
    return redirect(url_for("show_main_view"))
