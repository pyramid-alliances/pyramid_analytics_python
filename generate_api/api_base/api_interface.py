import copy
from enum import IntEnum
import requests
from requests.exceptions import HTTPError
import json
from json.decoder import JSONDecodeError
import logging
from pydantic import BaseModel

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

import typing 

log = logging.getLogger(__name__)
from uuid import UUID


class APIException(Exception):
    pass


class Grant(BaseModel):
    domain: str = None
    token: str = None


class PasswordGrant(Grant):
    username: str
    password: str


class TokenGrant(Grant):
    pass


_session = None


class ApiInterface:
    def __init__(self, domain: str = None):
        self.domain: str = domain
        self.token: str = None
        self.debug: bool = False
        self.called_endpoints = None

        if log.getEffectiveLevel() is logging.DEBUG:
            self.called_endpoints = set()
            log.warn("LogLevel is Debug! API will log ALL requests and responses!")
            log.warn("Unless you are debugging you do not want this!")

    # def login(self, username: str, password: str):
    #    return self.authenticate(PasswordGrant(username=username, password=password))

    def authenticate(self, credential: PasswordGrant):
        self.domain = credential.domain or self.domain
        try:
            self.token = self._call_api(
                "/API2/auth/authenticateUser",
                {
                    "data": {
                        "userName": credential.username,
                        "password": credential.password,
                    }
                },
            )
        except HTTPError as err:
            raise APIException("Invalid Credentials") from err

    def validate_grant(self, credential: TokenGrant):
        return
        """
        self.domain = credential.domain
        self.token = credential.token
        try:
            self.getMe()
        except HTTPError as err:
            raise APIException('Invalid Token') from err
        """

    def _call_api(self, endpoint: str, data: Any, method: str = "POST"):
        if self.called_endpoints != None:
            self.called_endpoints.add(endpoint)

        if not data:
            data = {}
        data["auth"] = self.token
        # print(repr(data))
        res = requests.request(method=method, url=f"{self.domain}{endpoint}", json=data)
        log.debug(f"{endpoint}")
        log.debug(json.dumps(data, indent=2))
        try:
            res.raise_for_status()
        except HTTPError as her:
            log.error(her)
            log.error(f"error content: {res.text}")
            raise her
        log.debug(f"status -> {res.status_code}")
        try:
            _json = res.json()
            if "error" in _json:
                raise APIException(
                    f'Unexpected error returned from server: {_json.get("error")}'
                )
            log.debug(json.dumps(_json, indent=2))
            return _json
        except JSONDecodeError:
            log.debug(res.text)
            return res.text

    def __ignore_self(self, locals: Dict):
        return {k: v for k, v in locals.items() if k != "self"}

    def __ignore_nulls(self, d: Dict):
        return {k: v for k, v in d.items() if v != None}




def setup_logging():
    logging.basicConfig(filename="pyramid.log", encoding="utf-8", level=logging.DEBUG)


def call_api(endpoint: str, data: Dict, response_type: Any = None):
    if not _session:
        raise APIException("You need to create a session first. ")
    clean_data = None
    if data:
        clean_data = {}
        for k,v in data.items():
            if isinstance(v, IntEnum):
                v = int(v)
            elif isinstance(v, UUID):
                v = str(v)
            elif isinstance(v, BaseModel):
                v = v.dict()
            clean_data[k] = v

    print(f"calling {endpoint} data: '{clean_data}' response_type : {response_type}")
    response = _session._call_api(endpoint, clean_data)
    result = None
    if response_type:
        if "data" in response:
            #import ipdb;ipdb.set_trace()
            if typing.get_origin(response_type) == list:
                elem_type = typing.get_args(response_type)[0]
                print(f"elem type {elem_type}")
                result = [ elem_type(**elem) for elem in response["data"]]
            else:
                result = response_type(**response["data"])
        else:
            raise(APIException("invalid response : {}".format(response)))
    else:
        return response
    #print(result)
    return result


def get_session(domain: str) -> ApiInterface:
    global _session
    if not _session:
        _session = ApiInterface(domain=domain)
    return _session


def clear_session() -> None:
    global _session
    _session = None

__all__ = (
    "ApiInterface",
    "APIException",
    "PasswordGrant",
    "TokenGrant",
    "get_session",
    "setup_logging",
)
