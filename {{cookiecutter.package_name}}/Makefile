all: run

clean:
	rm -rf ../.venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	pipenv --three --bare install -e {{cookiecutter.package_name}}

run: venv
	export FLASK_APP={{cookiecutter.package_name}}; {{cookiecutter.package_name.upper()}}_SETTINGS=../settings.cfg pipenv --bare run flask run

test: venv
	cd ..; {{cookiecutter.package_name.upper()}}_SETTINGS=../settings.cfg pipenv --bare run python -m unittest discover -s tests

sdist: venv test
	../.venv/bin/python setup.py sdist
