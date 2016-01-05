#!/usr/bin/env python

"""
flask-extensions.blueprints
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The (V)eiws in MVC!

:copyright: (c) 2016 Michael Hoyt. <@pr0xmeh>
:license: MIT
"""

from flask import Blueprint, render_template

blueprints = Blueprint('blueprints', __name__, template_folder='templates')

@blueprints.route('/')
def home():
    return render_template('home.jinja2')
