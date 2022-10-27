import sys
import os
import logging

os.environ["PYTHONBREAKPOINT"] = "pdbr.set_trace"

sys.path.append(os.path.realpath("."))

logging.getLogger('faker.factory').setLevel(logging.ERROR)


pytest_plugins = [
   "fixtures.kubernetes",
   "fixtures.pyramid",
   "fixtures.browser"
  ]


def pytest_addoption(parser):
    parser.addoption(
        "--local", action="store_true", help="Run locally with k8s proxy."
    )

def pytest_addoption(parser):
    parser.addoption(
        "--pyramid_settings", action="store_true", help="pyramid settings json file for Pyramid."
    )


logging.basicConfig(level=logging.INFO,
        format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s',)