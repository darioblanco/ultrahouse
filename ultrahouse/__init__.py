import flask

from ultrahouse.settings import DATABASE


def create_app(db_path=DATABASE, debug=False, testing=False):
    """Returns a flask app object with an assigned db and api manager"""
    app = flask.Flask(__name__)
    app.config['DEBUG'] = debug
    app.config['TESTING'] = testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)

    from ultrahouse.model import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from ultrahouse.api import api_manager, create_endpoints
    api_manager.init_app(app, flask_sqlalchemy_db=db)
    create_endpoints()

    return app
