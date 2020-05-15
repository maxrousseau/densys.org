#-*- coding: utf-8 -*-
import os
import tempfile

import pytest
from densys import create_app
import coverage

@pytest.fixture
def app():
    app = create_app({
        'TESTING':True
    })

    yield app #from flask doc

@pytest.fixture
def client():
    return app.test_client()

@pytest.fixture
def runner():
    return app.test_cli_runner()


