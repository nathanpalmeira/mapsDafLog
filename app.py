# import discovery
from flask import Flask,render_template, request, redirect, url_for, session
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib.parse
import base64
# from bs4 import BeautifulSoup
from datetime import datetime,timedelta
import json
# import xmltodict


app = Flask(__name__)
app.config['SECRET_KEY'] = 'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

@app.route("/")
def hello():
    return redirect(url_for('insulinaNph10'))

    # pass

@app.route("/insulinaNph10")
def insulinaNph10():
    return render_template("insulinaNph10.html", acao="BEM")


@app.route("/insulinaRegular10")
def insulinaRegular10():
    return render_template("insulinaRegular10.html", acao="BEM")



@app.route("/insulinaNphTubetes3")
def insulinaNphTubetes3():
    return render_template("insulinaNphTubetes3.html", acao="BEM")

@app.route("/insulinaRegularTubetes3")
def insulinaRegularTubetes3():
    return render_template("insulinaRegularTubetes3.html", acao="BEM")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
