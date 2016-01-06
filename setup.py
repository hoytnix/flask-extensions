from setuptools import setup

setup(
    name='flask-extensions-org',
    version='1.0',
    py_modules=['flask_extensions'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        run=manage:cli
    ''',
)
