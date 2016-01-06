#!/usr/bin/env python

"""
flask-extensions.manage
~~~~~~~~~~~~~~~~~~~~~~~

Application setup-and-teardown.

:copyright: (c) 2016 Michael Hoyt. <@pr0xmeh>
:license: MIT
"""

import os

from flask import Flask

from .blueprints import blueprints
from .config import Config
from .extensions import db
from .utils import abs_templates


def create_app():
    config = Config()

    app = Flask(import_name=__name__, template_folder=abs_templates)
    app.config.from_object(config)
    app.register_blueprint(blueprints, url_prefix='')

    db.init_app(app)

    return app




