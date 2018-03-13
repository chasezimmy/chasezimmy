# -*- coding: utf-8 -*-
from flask import Flask, request, send_from_directory, render_template, jsonify
import os
import json
from helper import Face

app = Flask(__name__)
face = Face()


@app.route('/')
def index():
    work_json = os.path.join(app.static_folder, "", "work.json")
    work = json.load(open(work_json))['work']

    return render_template('index.html', work=work)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', face="¯\_(ツ)_/¯".decode("utf8")), 404


@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/face')
def lenny_face():
    return jsonify(face=face.lenny_me())


if __name__ == "__main__":
    app.run()
