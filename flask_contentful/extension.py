#
# Flask-Contentful
#
# Copyright (C) 2018 Boris Raicheff
# All rights reserved
#


import logging

from contentful import Client
from flask import Response


logger = logging.getLogger('Flask-Contentful')


class Contentful(object):
    """
    Flask-Contentful

    https://pypi.python.org/pypi/flask-contentful

    https://flask-contentful.readthedocs.io

    :param app: Flask app to initialize with. Defaults to `None`
    """

    client = None

    def __init__(self, app=None, blueprint=None):
        if app is not None:
            self.init_app(app, blueprint)

    def init_app(self, app, blueprint=None):
        space_id, access_token = (app.config.get(name) for name in ('CONTENTFUL_SPACE_ID', 'CONTENTFUL_DELIVERY_TOKEN'))
        self.client = Client(space_id=space_id, access_token=access_token)
        if blueprint is not None:
            blueprint.add_url_rule('/contentful', 'contentful', self.handle_webhook, methods=('POST',))

    def handle_webhook(self):
        # https://buttercms.com/docs/api/?python#webhooks
        # TODO
        return Response()

    def __getattr__(self, name):
        return getattr(self.client, name)


# EOF
