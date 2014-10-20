import pytest

import falcon
from falcon.testing.helpers import create_environ
from falcon.testing.srmock import StartResponseMock


class App(object):
    def __init__(self):
        self.api = falcon.API()
        self.srmock = StartResponseMock()

        before = getattr(self, 'before', None)
        if callable(before):
            before()

    def _simulate_request(self, path, decode=None, **kwargs):
        """See falcon.testing.base.TestBase.simulate_request"""
        if not path:
            path = '/'

        result = self.api(create_environ(path=path, **kwargs),
                          self.srmock)

        if decode is not None:
            if not result:
                return ''

            return result[0].decode(decode)

        return result

    def get(self, path, decode=None, **kwargs):
        return self._simulate_request(path, decode=None, method='GET',
                                      **kwargs)

    def post(self, path, decode=None, **kwargs):
        return self._simulate_request(path, decode=None, method='POST',
                                      **kwargs)

    def put(self, path, decode=None, **kwargs):
        return self._simulate_request(path, decode=None, method='PUT',
                                      **kwargs)

    def delete(self, path, decode=None, **kwargs):
        return self._simulate_request(path, decode=None, method='DELETE',
                                      **kwargs)

    def destroy(self):
        after = getattr(self, 'after', None)
        if callable(after):
            after()


@pytest.fixture(scope='session')
def app():
    """Session-wide test `Falcon` application."""
    test_app = App()

    def fin():
        """Teardown code for destroying the test application"""
        test_app.destroy()

    return test_app
