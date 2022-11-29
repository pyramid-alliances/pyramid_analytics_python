default: build

clean:
	rm -rf pyramid_api dist build pyramid_analytics_api.egg-info

venv:
	python -m venv venv
	./venv/bin/pip install -r requirements.txt

build: clean
	python generate_api/gen_api.py

test:
	PA_TEST_SETTINGS=test_settings.json pytest