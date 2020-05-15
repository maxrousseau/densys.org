#-*- coding: utf-8 -*-
from densys import create_app

def test_config():
    assert not create_app().testing

