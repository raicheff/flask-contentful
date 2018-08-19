#
# Flask-Contentful
#
# Copyright (C) 2018 Boris Raicheff
# All rights reserved
#


from setuptools import find_packages, setup


setup(
    name='Flask-Contentful',
    version='0.1.0',
    description='Flask-Contentful',
    author='Boris Raicheff',
    author_email='b@raicheff.com',
    url='https://github.com/raicheff/flask-contentful',
    install_requires=('contentful', 'flask', 'six'),
    packages=find_packages(),
)


# EOF
