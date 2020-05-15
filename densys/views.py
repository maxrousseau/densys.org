#-*- coding: utf-8 -*-
import os

from flask import (
    Flask,  make_response, request, Blueprint, url_for,
    redirect, render_template
)

bp = Blueprint('views', __name__, url_prefix='')

@bp.route('/')
def vw_home():
    return render_template("home.html")

@bp.route('/news')
def vw_news():
    return render_template("news.html")

@bp.route('/about')
def vw_about():
    return render_template("about.html")

@bp.route('/projects')
def vw_projects():
    return render_template("projects.html")

@bp.route('/projects/pfla')
def vw_proj_pfla():
    return render_template("pfla.html")

