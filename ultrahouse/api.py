# -*- coding: utf-8 -*-
# Copyright 2014, wywy GmbH

import json

import falcon

from ultrahouse import model


def deserialize(req, resp, resource, params):
    # req.stream corresponds to the WSGI wsgi.input environ variable,
    # and allows you to read bytes from the request body.
    #
    # See also: PEP 3333
    body = req.stream.read()
    if not body:
        raise falcon.HTTPBadRequest('Empty request body',
                                    'A valid JSON document is required.')

    try:
        params['doc'] = json.loads(body.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        raise falcon.HTTPError(falcon.HTTP_753,
                               'Malformed JSON',
                               'Could not decode the request body. The '
                               'JSON was incorrect or not encoded as UTF-8.')


def serialize(req, resp, resource):
    resp.body = json.dumps(req.context['doc'])


class Device:
    @falcon.after(serialize)
    def on_get(self, req, resp, name):
        """Handles GET requests"""
        device = model.session.query.filter(Device.name == name)
        if device is None:
            raise falcon.HTTPError(falcon.HTTP_404,
                                   "Device {} not found".format(name))

        resp.status = falcon.HTTP_200
        req.context['doc'] = {
            'id': device.id,
            'name': device.name,
            'mac': device.mac
        }

    @falcon.before(deserialize)
    def on_post(self, req, resp, name, doc):
        """Handles POST requests"""
        resp.status = falcon.HTTP_201
        device = model.Device(name=doc['name'], mac=doc['mac'])
        model.session.add(device)
        model.session.commit()

    def on_delete(self, req, resp, name):
        """Handles DELETE requests"""
        resp.status = falcon.HTTP_204
        device = model.session.query.filter(Device.name == name)
        model.session.delete(device)
        model.session.commit()


# Callable WSGI app
app = falcon.API()

# Resources
devices = Device()

# Handle all requests to the URL path
app.add_route('/api/device/{name}', devices)
