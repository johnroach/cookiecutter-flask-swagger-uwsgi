import os
from flask import Flask
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.config.from_object('{{cookiecutter.package_name}}.default_settings')
# NOT SURE IF WE WOULD ACTUALLY BRING A FILE FOR CONFIGURATIONS I WOULD RATHER DO
# THIS VIA ENVIRONMENT VARIABLES THAT GET INJECTED VIA KUBE FILES
#app.config.from_envvar('{{cookiecutter.package_name.upper()}}_SETTINGS')

import {{cookiecutter.package_name}}.views
