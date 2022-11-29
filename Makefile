default: build

clean:
	rm -rf pyramid_api dist build pyramid_analytics_api.egg-info

deepclean: clean
	rm -rf venv

venv:
	python -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt

build: clean venv
	./venv/bin/python generate_api/gen_api.py

test: build
	PA_TEST_SETTINGS=test_settings.json ./venv/bin/pytest

dist: build test
	./venv/bin/python setup.py bdist_wheel