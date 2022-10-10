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


def login(domain: str, username: str, password: str, set_active: bool = True) -> ApiInterface:
    session = ApiInterface(domain=domain)
    session.authenticate(PasswordGrant(username=username, password=password))
    if set_active:
        set_session(session)
    return session
