Create python python modules from the REST documentation online

# create venv
$ python -m venv venv

# install requirements
$ ./venv/bin/pip install -r requirements.txt

# download api html docs and save in local "cache" dir
# output is written to "pyramid_api"
$ ./venv/bin/python gen_api.py

The html is parsed with BeautifulSoup4 and the code is generated with
the Jinja2 template engine.

When generating the api_base directory is merged with the generated files
to provide the final generated module. 
After generating it, it can be moved up to the parent directory to be used
