#!/usr/bin/env python3

#Documentation
#See also https://www.python-boilerplate.com/flask

from os import environ 
from app import create_app

if __name__ == "__main__":
    port = int(environ.get("PORT", 8000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)