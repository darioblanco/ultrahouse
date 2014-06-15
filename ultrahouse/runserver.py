#!/usr/bin/env python
import argparse

from ultrahouse import create_app


if __name__ == '__main__':
    """Runs the ultrahouse application"""
    parser = argparse.ArgumentParser(description='Runs ultrahouse webserver')
    parser.add_argument("--host", type=str, default='localhost',
                        help="Webserver host")
    parser.add_argument("--port", type=int, default=7777,
                        help="Webserver port")
    parser.add_argument("--debug", action="store_true", default=False,
                        help="Set debug mode")
    args_dict = vars(parser.parse_args())

    app = create_app(debug=args_dict['debug'])
    app.run(host=args_dict['host'], port=args_dict['port'])
