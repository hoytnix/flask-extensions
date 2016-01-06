#!/usr/bin/env python

"""
flask-extensions.models
~~~~~~~~~~~~~~~~~~~~~~~

The (M)odels in MVC!

:copyright: (c) 2016 Michael Hoyt. <@pr0xmeh>
:license: MIT
"""

from .extensions import db
from .utils import slugify


class Extension(db.Model):
    __tablename__ = 'extensions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    description = db.Column(db.Text())
    version = db.Column(db.Text())

    github = db.Column(db.Text())  # user/repo
    stars = db.Column(db.Integer)
    forks = db.Column(db.Integer)
    coverage = db.Column(db.Integer)

    @property
    def slug(self):
        return slugify(self.title)

    @property
    def ahref(self):
        return '<a href="/{}/{}-{}">{}</a>'.format(self.__tablename__,
                                                  self.id,
                                                  self.slug,
                                                  self.title)

    def __repr__(self):
        return '<{} [{}]>'.format(self.__name__, self.id)


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())

    github = db.Column(db.Text())

    @property
    def slug(self):
        return slugify(self.title)

    @property
    def ahref(self):
        return '<a href="/{}/{}-{}">{}</a>'.format(self.__tablename__,
                                                  self.id,
                                                  self.slug,
                                                  self.title)

    def __repr__(self):
        return '<{} [{}]>'.format(self.__name__, self.id)


class ProjectExtensions(db.Model):
    __tablename__ = 'project_extensions'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer)
    extension_id = db.Column(db.Integer)

    def __repr__(self):
        return '<{} [{}]>'.format(self.__name__, self.id)



