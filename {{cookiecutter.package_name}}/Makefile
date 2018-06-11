all: run

clean:
	rm -rf ../.venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	cd ..;pipenv --three --bare install -e {{cookiecutter.package_name}}

run: venv
	export FLASK_APP={{cookiecutter.package_name}}; {{cookiecutter.package_name.upper()}}_SETTINGS=../settings.cfg; pipenv --bare run python -m {{cookiecutter.package_name}}

test: venv
	cd ..; {{cookiecutter.package_name.upper()}}_SETTINGS=../settings.cfg pipenv --bare run python -m unittest discover -s tests

sdist: venv test
	rm -rf dist; pipenv --bare run python setup.py sdist

build-container: sdist
	cd dist;tar -xvf {{cookiecutter.package_name}}-$(version).tar.gz; \
	mv {{cookiecutter.package_name}}-$(version) {{cookiecutter.package_name}}; \
	cd ..; docker build . -t {{cookiecutter.package_name}}:$(version)
