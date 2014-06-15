from flask.ext.restless import APIManager

from ultrahouse import model


api_manager = APIManager()


def create_endpoints():
    """Sets api endpoints for each specified SQLAlchemy model"""
    # /api/device
    api_manager.create_api(model.Device,
                           methods=['GET', 'POST', 'PUT', 'DELETE'])
