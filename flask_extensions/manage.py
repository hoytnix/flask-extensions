#!/usr/bin/env python

"""
flask-extensions.manage
~~~~~~~~~~~~~~~~~~~~~~~

Provide commands for managing the application.

:copyright: (c) 2016 Michael Hoyt. <@pr0xmeh>
:license: MIT
"""

from flask import Flask
from flask_script import Manager, Server

from blueprints import blueprints

app = Flask(import_name='flask_extensions', template_folder='../templates')
app.register_blueprint(blueprints, url_prefix='')

manager = Manager(app)

manager.add_command('runserver', Server('0.0.0.0',
        port = 12345,
        use_debugger = True,
        use_reloader = True
    )
)

if __name__ == '__main__':
    manager.run()
