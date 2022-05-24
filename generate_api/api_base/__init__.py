from .api_interface import *
from . import enum
from . import objects

from . import access
from . import auth
from . import content
from . import dataSources
from . import notification
from . import query
from . import tasks


def login(domain: str, username: str, password: str) -> ApiInterface:
    session = get_session(domain=domain)
    session.authenticate(PasswordGrant(username=username, password=password))
    return session
