# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body44(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None, flight_id: str=None, return_flight_id: str=None, booking_id: str=None):  # noqa: E501
        """Body44 - a model defined in Swagger

        :param token: The token of this Body44.  # noqa: E501
        :type token: str
        :param flight_id: The flight_id of this Body44.  # noqa: E501
        :type flight_id: str
        :param return_flight_id: The return_flight_id of this Body44.  # noqa: E501
        :type return_flight_id: str
        :param booking_id: The booking_id of this Body44.  # noqa: E501
        :type booking_id: str
        """
        self.swagger_types = {
            'token': str,
            'flight_id': str,
            'return_flight_id': str,
            'booking_id': str
        }

        self.attribute_map = {
            'token': 'token',
            'flight_id': 'flight_id',
            'return_flight_id': 'return_flight_id',
            'booking_id': 'booking_id'
        }
        self._token = token
        self._flight_id = flight_id
        self._return_flight_id = return_flight_id
        self._booking_id = booking_id

    @classmethod
    def from_dict(cls, dikt) -> 'Body44':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_44 of this Body44.  # noqa: E501
        :rtype: Body44
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body44.


        :return: The token of this Body44.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body44.


        :param token: The token of this Body44.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def flight_id(self) -> str:
        """Gets the flight_id of this Body44.


        :return: The flight_id of this Body44.
        :rtype: str
        """
        return self._flight_id

    @flight_id.setter
    def flight_id(self, flight_id: str):
        """Sets the flight_id of this Body44.


        :param flight_id: The flight_id of this Body44.
        :type flight_id: str
        """

        self._flight_id = flight_id

    @property
    def return_flight_id(self) -> str:
        """Gets the return_flight_id of this Body44.


        :return: The return_flight_id of this Body44.
        :rtype: str
        """
        return self._return_flight_id

    @return_flight_id.setter
    def return_flight_id(self, return_flight_id: str):
        """Sets the return_flight_id of this Body44.


        :param return_flight_id: The return_flight_id of this Body44.
        :type return_flight_id: str
        """

        self._return_flight_id = return_flight_id

    @property
    def booking_id(self) -> str:
        """Gets the booking_id of this Body44.


        :return: The booking_id of this Body44.
        :rtype: str
        """
        return self._booking_id

    @booking_id.setter
    def booking_id(self, booking_id: str):
        """Sets the booking_id of this Body44.


        :param booking_id: The booking_id of this Body44.
        :type booking_id: str
        """

        self._booking_id = booking_id
