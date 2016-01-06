#!/usr/bin/env python

"""
flask-extensions.blueprints
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The (V)eiws in MVC!

:copyright: (c) 2016 Michael Hoyt. <@pr0xmeh>
:license: MIT
"""

from flask import Blueprint, render_template

from .models import Extension, Project, ProjectExtensions


blueprints = Blueprint('blueprints', __name__, template_folder='templates')


@blueprints.route('/')
def home():
    return render_template('home.jinja2')


@blueprints.route('/extensions')
def extension_list():
    extensions = Extension.query.all()

    return render_template('extension_list.jinja2', extensions=extensions)


@blueprints.route('/extensions/<int:extension_id>')
@blueprints.route('/extensions/<int:extension_id>-<slug>')
def extension_detail(extension_id, slug=None):
    extension = Extension.query.get(extension_id)

    return render_template('extension_detail.jinja2', extension=extension)


@blueprints.route('/projects')
def project_list():
    projects = Project.query.all()

    return render_template('project_list.jinja2', projects=projects)


@blueprints.route('/projects/<int:project_id>')
@blueprints.route('/projects/<int:project_id>-<slug>')
def project_detail(project_id, slug=None):
    project = Project.query.get(project_id)

    return render_template('project_detail.jinja2', project=project)



