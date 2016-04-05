# Flask Boilerplate

This is boilerplate so you can get started quickly on a basic Flask app running Python 3.4.3.

## Setup

1. Create and activate a virtualenv: `pyvenv env`, `source env/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Below the project root, create a directory `instance` containing an empty `config.py`. This can be used for storing sensitive information, such as passwords. Do not version control this directory.
4. Edit `/config.py` (below the project root) as your project requires. Separate configurations for development, testing, and production are included.

## Usage

This boilerplate uses the `flask-script` extension to provide a command-line interface to the app. Out of the box, it includes the command `runserver`, which runs the app by default at `localhost:5000`.

To run in development mode: `python manage.py runserver`

To run in production mode: `python manage.py -c production runserver`

I have included basic MongoDB support (via `flask-mongoengine`), as well as Bootstrap and jQuery (via CDN) on the frontend.
