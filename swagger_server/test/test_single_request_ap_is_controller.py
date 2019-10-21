# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.body2 import Body2  # noqa: E501
from swagger_server.models.body3 import Body3  # noqa: E501
from swagger_server.models.body4 import Body4  # noqa: E501
from swagger_server.models.body5 import Body5  # noqa: E501
from swagger_server.models.body6 import Body6  # noqa: E501
from swagger_server.models.body7 import Body7  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.internet import Internet  # noqa: E501
from swagger_server.models.network import Network  # noqa: E501
from swagger_server.models.topup import Topup  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSingleRequestAPIsController(BaseTestCase):
    """SingleRequestAPIsController integration test stubs"""

    def test_api_use_adsl_ul_post(self):
        """Test case for api_use_adsl_ul_post

        
        """
        body = Topup()
        response = self.client.open(
            '/api/use/adsl-ul/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_alisha_communication_post(self):
        """Test case for api_use_alisha_communication_post

        
        """
        body = Body4()
        response = self.client.open(
            '/api/use/alisha-communication/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_cleartv_post(self):
        """Test case for api_use_cleartv_post

        
        """
        body = Body2()
        response = self.client.open(
            '/api/use/cleartv/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_hons_post(self):
        """Test case for api_use_hons_post

        
        """
        body = Network()
        response = self.client.open(
            '/api/use/hons/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_infonet_communication_post(self):
        """Test case for api_use_infonet_communication_post

        
        """
        body = Body5()
        response = self.client.open(
            '/api/use/infonet-communication/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_khalti_topup_post(self):
        """Test case for api_use_khalti_topup_post

        
        """
        body = Topup()
        response = self.client.open(
            '/api/use/khalti-topup/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_landline_post(self):
        """Test case for api_use_landline_post

        
        """
        body = Topup()
        response = self.client.open(
            '/api/use/landline/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_method_post(self):
        """Test case for api_use_method_post

        
        """
        body = Body()
        response = self.client.open(
            '/api/use/{method}/'.format(method='method_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_metrolink_post(self):
        """Test case for api_use_metrolink_post

        
        """
        body = Body6()
        response = self.client.open(
            '/api/use/metrolink/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_ncell_post(self):
        """Test case for api_use_ncell_post

        
        """
        body = Topup()
        response = self.client.open(
            '/api/use/ncell/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_ntc_post(self):
        """Test case for api_use_ntc_post

        
        """
        body = Topup()
        response = self.client.open(
            '/api/use/ntc/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_pokhara_internet_post(self):
        """Test case for api_use_pokhara_internet_post

        
        """
        body = Body3()
        response = self.client.open(
            '/api/use/pokhara-internet/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_royal_network_post(self):
        """Test case for api_use_royal_network_post

        
        """
        body = Network()
        response = self.client.open(
            '/api/use/royal-network/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_service_slug_post(self):
        """Test case for api_use_service_slug_post

        Capital Share
        """
        body = Body7()
        response = self.client.open(
            '/api/use/{service_slug}/'.format(service_slug='service_slug_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_simtv_post(self):
        """Test case for api_use_simtv_post

        
        """
        body = Body1()
        response = self.client.open(
            '/api/use/simtv/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_sky_topup_post(self):
        """Test case for api_use_sky_topup_post

        
        """
        body = Internet()
        response = self.client.open(
            '/api/use/sky-topup/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_smartcell_post(self):
        """Test case for api_use_smartcell_post

        
        """
        body = Topup()
        response = self.client.open(
            '/api/use/smartcell/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_subisu_post(self):
        """Test case for api_use_subisu_post

        
        """
        body = Internet()
        response = self.client.open(
            '/api/use/subisu/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_virtual_network_post(self):
        """Test case for api_use_virtual_network_post

        
        """
        body = Network()
        response = self.client.open(
            '/api/use/virtual-network/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_web_network_post(self):
        """Test case for api_use_web_network_post

        
        """
        body = Network()
        response = self.client.open(
            '/api/use/web-network/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_websurfer_topup_post(self):
        """Test case for api_use_websurfer_topup_post

        
        """
        body = Internet()
        response = self.client.open(
            '/api/use/websurfer-topup/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
