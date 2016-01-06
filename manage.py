#!/usr/bin/env python

"""
flask-extensions
~~~~~~~~~~~~~~~~

Commands for managing the application.

:copyright: (c) 2016 Michael Hoyt. <@pr0xmeh>
:license: MIT
"""

import click

from flask_extensions.app import create_app
from flask_extensions.extensions import db
from flask_extensions.utils import all_models


@click.group()
@click.version_option()
def cli():
    """This is a doc-string.
    """


@cli.command('start')
def run_server():
    app = create_app()
    app.run(host='0.0.0.0', port=13337, debug=True)


@cli.command('resetdb')
def test(): 
    all_models()

    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()





