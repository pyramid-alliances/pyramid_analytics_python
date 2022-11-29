default: build

clean:
	rm -rf pyramid_api dist build pyramid_analytics_api.egg-info

build: clean
	python generate_api/gen_api.py