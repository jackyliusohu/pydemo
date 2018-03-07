# -*- coding:utf-8 -*-
from flask import render_template

from web import app
from .login import authorize

__author__ = 'Rocky Peng'


@app.route("/homes", methods=["GET"])
@authorize
def homes():
    return render_template("homes.html")


@app.route("/homes/<int:id>", methods=["GET"])
@authorize
def homes_id(id):
    return render_template("home_detail.html")


@app.route("/home/create", methods=["GET"])
@authorize
def home_creation():
    return render_template("home_create.html")


@app.route("/home/<int:id>/group", methods=["GET"])
@authorize
def home_group(id):
    return render_template("home_detail.html")
