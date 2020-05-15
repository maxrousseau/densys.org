#-*- coding: utf-8 -*-
import os

from flask import Flask, make_response, jsonify

from . import views

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=None,
    )

    if test_config==None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_pyfile(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # get views
    app.register_blueprint(views.bp)

    @app.errorhandler(404)
    def not_found(error):
        """improved error message
        This method will returns an error message.

        Parameters
        ----------
        error : string

        Returns
        ------
        make_response : JSON entry
        """
        return make_response(jsonify({'error':'Not found'}), 404)

    return app
