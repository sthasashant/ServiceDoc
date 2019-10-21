# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body37(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None, request_id: str=None, insurance_slug: str=None):  # noqa: E501
        """Body37 - a model defined in Swagger

        :param token: The token of this Body37.  # noqa: E501
        :type token: str
        :param request_id: The request_id of this Body37.  # noqa: E501
        :type request_id: str
        :param insurance_slug: The insurance_slug of this Body37.  # noqa: E501
        :type insurance_slug: str
        """
        self.swagger_types = {
            'token': str,
            'request_id': str,
            'insurance_slug': str
        }

        self.attribute_map = {
            'token': 'token',
            'request_id': 'request_id',
            'insurance_slug': 'insurance_slug'
        }
        self._token = token
        self._request_id = request_id
        self._insurance_slug = insurance_slug

    @classmethod
    def from_dict(cls, dikt) -> 'Body37':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_37 of this Body37.  # noqa: E501
        :rtype: Body37
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body37.


        :return: The token of this Body37.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body37.


        :param token: The token of this Body37.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def request_id(self) -> str:
        """Gets the request_id of this Body37.


        :return: The request_id of this Body37.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id: str):
        """Sets the request_id of this Body37.


        :param request_id: The request_id of this Body37.
        :type request_id: str
        """

        self._request_id = request_id

    @property
    def insurance_slug(self) -> str:
        """Gets the insurance_slug of this Body37.


        :return: The insurance_slug of this Body37.
        :rtype: str
        """
        return self._insurance_slug

    @insurance_slug.setter
    def insurance_slug(self, insurance_slug: str):
        """Sets the insurance_slug of this Body37.


        :param insurance_slug: The insurance_slug of this Body37.
        :type insurance_slug: str
        """

        self._insurance_slug = insurance_slug
