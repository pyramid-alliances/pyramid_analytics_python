import pytest

import six.moves.urllib.request as urllib_request

import logging
log = logging.getLogger(__name__)



@pytest.fixture
def kubernetes():
   # Configs can be set in Configuration class directly or using helper utility
   log.debug("getting k8s client")
   config.load_kube_config()
   return client

