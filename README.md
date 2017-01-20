# Flask Boilerplate

This is boilerplate so you can get started quickly on a decoupled app with Flask serving a RESTful API on Python 3.5. I have included testing (via `flask-testing`), authentication (via `flask-security`) and MongoDB support (via `flask-mongoengine`).

## Setup

1. Create and activate a virtualenv: `pyvenv env`, `source env/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Below the project root, create a directory `instance` containing a file `config.py`. This can be used for storing sensitive information, such as passwords. It should have at minimum `MONGODB_USERNAME`, `MONGODB_PASSWORD`, and `SECRET_KEY` [(see here)](http://flask.pocoo.org/docs/0.12/quickstart/#sessions) defined. Do not version control this directory.
4. Edit `/config.py` (below the project root) as your project requires. Separate configurations for development, testing, and production are included.

## Usage

This boilerplate uses the `flask-script` extension to provide a command-line interface to the app. Out of the box, it includes the command `runserver`, which runs the app by default at `localhost:5000`.

To run in development mode: `python -m manage runserver`

To run in production mode: `python -m manage -c production runserver`

To run tests: `python -m manage test`

## Frontend

This is designed to work alongside [vuejs-boilerplate](https://github.com/colingorrie/vuejs-boilerplate).
