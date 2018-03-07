#!/usr/local/bin/python
# -*- coding:utf-8 -*-
from web import db
from web.utils.jsonencoder import JsonSerializer

__author__ = 'Rocky Peng'


rel_user_home = db.Table(
    "rel_user_home",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("home_id", db.Integer, db.ForeignKey("homes.id")),
    db.Column("created_at", db.DateTime, default=db.func.now()),
    db.Column("updated_at", db.DateTime, default=db.func.now(),
              onupdate=db.func.now()),
)


class Home(JsonSerializer, db.Model):
    __json_hidden__ = ["deploys", "users"]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    ssh_host = db.Column(db.String(32))
    ssh_port = db.Column(db.Integer)
    ssh_method = db.Column(db.Integer())
    ssh_user = db.Column(db.String(64))
    ssh_pass = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(),
                           onupdate=db.func.now())

    #users = db.relationship("Users", secondary=rel_user_home,
    #                        backref=db.backref("homes", lazy="dynamic"))
