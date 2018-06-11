# flask-swagger-uwsgi

[![Build Status](https://travis-ci.org/JohnRoach/cookiecutter-flask-swagger-uwsgi.svg?branch=master)](https://travis-ci.org/JohnRoach/cookiecutter-flask-swagger-uwsgi)

This is an **opinionated** [Flask](http://flask.pocoo.org) based project. It is meant to be used with Kubernetes type orchestration solutions as well as API Gateway solutions that will use Open API 2.0 specification(formerly known as Swagger).


## Usage

Install [cookiecutter](https://github.com/audreyr/cookiecutter):

    pipenv install --dev --three cookiecutter

Create your application from this template:

    cookiecutter https://github.com/JohnRoach/cookiecutter-flask-swagger-uwsgi.git

All set! Run the application:

    cd yourapplication
    make run

And then open it at [http://127.0.0.1:3040/](http://127.0.0.1:3040/)


## Features

Included:

 - production-ready Flask application: root package, sample static resource, sample template and an index view,
   as per [Larger Applications](http://flask.pocoo.org/docs/0.12/patterns/packages/)

 - Docker file with uwsgi setup

 - setuptools configuration to package and release the application, as well as to develop locally, as per
   [Deploying with Setuptools](http://flask.pocoo.org/docs/0.12/patterns/distribute/)

 - configuration system, as per [Configuration Handling](http://flask.pocoo.org/docs/0.12/config/#config)

 - basic logging configuration, as per [Logging to a File](http://flask.pocoo.org/docs/0.12/errorhandling/#logging-to-a-file)

 - sample test and configuration necessary to run the tests, as per
   [The Testing Skeleton](http://flask.pocoo.org/docs/0.12/testing/#the-testing-skeleton)

 - Makefile with few typical tasks automated (see generated README for details)

Not included:

 - everything else: there is no SQLAlchemy, or MongoKit, or Bootstrap CSS, or React, or whatever else here;
   it is up to you to chose how to implement your application


# Contributions

If you do a change, use `make test` from root directory to test the updated template.


# Possible future improvements
 - find a cross-platform replacement to a Makefile
