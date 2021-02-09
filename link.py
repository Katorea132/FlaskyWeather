"""
Module with the unique and special purpose of avoiding
circular imports through a common link
"""
from flask import Flask
from flask_restful import Api
from flask_caching import Cache


app = Flask(__name__)
api = Api(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
