#!/usr/local/bin/python
# -*- coding:utf-8 -*-
from web import db
from web.models.homes import Home
from .base import Base
from web.utils.log import Logger
logger = Logger("home service")
__author__ = 'Rocky Peng'


class HomeService(Base):
    __model__ = Home
homes = HomeService()
