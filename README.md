# flask_app
use pip install -r reqs.txt
or install manually

install flask:
python -m pip install flask

install mongo:
python -m pip install pymongo
python -m pip install dnspython

install gitlab:
https://python-gitlab.readthedocs.io/en/stable/install.html
pip install --upgrade python-gitlab


set globals:
(windows)
set FLASK_APP=flask_app.py
set FLASK_ENV=development
(linux)
export FLASK_APP=flask_app.py
export FLASK_ENV=development

run web service:
flask run