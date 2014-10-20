# -*- coding: utf-8 -*-
# Copyright 2014, wywy GmbH


def test_list_device(app):
    body = app.get('/api/device/foo')
    assert body == []
    assert app.srmock.status == "404 Not Found"
