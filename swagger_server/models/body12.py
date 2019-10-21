# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body12(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None):  # noqa: E501
        """Body12 - a model defined in Swagger

        :param token: The token of this Body12.  # noqa: E501
        :type token: str
        """
        self.swagger_types = {
            'token': str
        }

        self.attribute_map = {
            'token': 'token'
        }
        self._token = token

    @classmethod
    def from_dict(cls, dikt) -> 'Body12':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_12 of this Body12.  # noqa: E501
        :rtype: Body12
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body12.


        :return: The token of this Body12.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body12.


        :param token: The token of this Body12.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token
