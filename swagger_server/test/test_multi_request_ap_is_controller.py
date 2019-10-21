# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body10 import Body10  # noqa: E501
from swagger_server.models.body11 import Body11  # noqa: E501
from swagger_server.models.body12 import Body12  # noqa: E501
from swagger_server.models.body13 import Body13  # noqa: E501
from swagger_server.models.body14 import Body14  # noqa: E501
from swagger_server.models.body15 import Body15  # noqa: E501
from swagger_server.models.body16 import Body16  # noqa: E501
from swagger_server.models.body17 import Body17  # noqa: E501
from swagger_server.models.body18 import Body18  # noqa: E501
from swagger_server.models.body19 import Body19  # noqa: E501
from swagger_server.models.body20 import Body20  # noqa: E501
from swagger_server.models.body21 import Body21  # noqa: E501
from swagger_server.models.body22 import Body22  # noqa: E501
from swagger_server.models.body23 import Body23  # noqa: E501
from swagger_server.models.body24 import Body24  # noqa: E501
from swagger_server.models.body25 import Body25  # noqa: E501
from swagger_server.models.body26 import Body26  # noqa: E501
from swagger_server.models.body27 import Body27  # noqa: E501
from swagger_server.models.body28 import Body28  # noqa: E501
from swagger_server.models.body29 import Body29  # noqa: E501
from swagger_server.models.body30 import Body30  # noqa: E501
from swagger_server.models.body31 import Body31  # noqa: E501
from swagger_server.models.body32 import Body32  # noqa: E501
from swagger_server.models.body33 import Body33  # noqa: E501
from swagger_server.models.body34 import Body34  # noqa: E501
from swagger_server.models.body35 import Body35  # noqa: E501
from swagger_server.models.body36 import Body36  # noqa: E501
from swagger_server.models.body37 import Body37  # noqa: E501
from swagger_server.models.body38 import Body38  # noqa: E501
from swagger_server.models.body39 import Body39  # noqa: E501
from swagger_server.models.body40 import Body40  # noqa: E501
from swagger_server.models.body41 import Body41  # noqa: E501
from swagger_server.models.body42 import Body42  # noqa: E501
from swagger_server.models.body43 import Body43  # noqa: E501
from swagger_server.models.body44 import Body44  # noqa: E501
from swagger_server.models.body45 import Body45  # noqa: E501
from swagger_server.models.body46 import Body46  # noqa: E501
from swagger_server.models.body47 import Body47  # noqa: E501
from swagger_server.models.body48 import Body48  # noqa: E501
from swagger_server.models.body49 import Body49  # noqa: E501
from swagger_server.models.body50 import Body50  # noqa: E501
from swagger_server.models.body51 import Body51  # noqa: E501
from swagger_server.models.body52 import Body52  # noqa: E501
from swagger_server.models.body53 import Body53  # noqa: E501
from swagger_server.models.body54 import Body54  # noqa: E501
from swagger_server.models.body8 import Body8  # noqa: E501
from swagger_server.models.body9 import Body9  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response4001 import InlineResponse4001  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMultiRequestAPIsController(BaseTestCase):
    """MultiRequestAPIsController integration test stubs"""

    def test_api_download_id_get(self):
        """Test case for api_download_id_get

        
        """
        query_string = [('token', 'token_example'),
                        ('is_base64', 'is_base64_example')]
        response = self.client.open(
            '/api/download/{id}'.format(id='id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_lookup_dishhome_get(self):
        """Test case for api_lookup_dishhome_get

        
        """
        query_string = [('token', 'token_example'),
                        ('casid', 'casid_example')]
        response = self.client.open(
            '/api/lookup/dishhome/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_products_kaspersky_get(self):
        """Test case for api_products_kaspersky_get

        
        """
        query_string = [('token', 'token_example')]
        response = self.client.open(
            '/api/products/kaspersky/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_addinfo_flight_post(self):
        """Test case for api_servicegroup_addinfo_flight_post

        
        """
        body = Body45()
        response = self.client.open(
            '/api/servicegroup/addinfo/flight/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_book_flight_post(self):
        """Test case for api_servicegroup_book_flight_post

        
        """
        body = Body44()
        response = self.client.open(
            '/api/servicegroup/book/flight/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_cancel_flight_post(self):
        """Test case for api_servicegroup_cancel_flight_post

        
        """
        body = Body47()
        response = self.client.open(
            '/api/servicegroup/cancel/flight/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_cancel_movie_post(self):
        """Test case for api_servicegroup_cancel_movie_post

        
        """
        body = Body52()
        response = self.client.open(
            '/api/servicegroup/cancel/movie/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_arhant_insurances_post(self):
        """Test case for api_servicegroup_commit_arhant_insurances_post

        
        """
        body = Body38()
        response = self.client.open(
            '/api/servicegroup/commit/arhant-insurances/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_arrownet_post(self):
        """Test case for api_servicegroup_commit_arrownet_post

        
        """
        body = Body24()
        response = self.client.open(
            '/api/servicegroup/commit/arrownet/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_classitech_post(self):
        """Test case for api_servicegroup_commit_classitech_post

        
        """
        body = Body22()
        response = self.client.open(
            '/api/servicegroup/commit/classitech/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_merotv_post(self):
        """Test case for api_servicegroup_commit_merotv_post

        
        """
        body = Body16()
        response = self.client.open(
            '/api/servicegroup/commit/merotv/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_midas_post(self):
        """Test case for api_servicegroup_commit_midas_post

        
        """
        body = Body31()
        response = self.client.open(
            '/api/servicegroup/commit/midas/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_movie_post(self):
        """Test case for api_servicegroup_commit_movie_post

        
        """
        body = Body53()
        response = self.client.open(
            '/api/servicegroup/commit/movie/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_nabil_invest_post(self):
        """Test case for api_servicegroup_commit_nabil_invest_post

        
        """
        body = Body42()
        response = self.client.open(
            '/api/servicegroup/commit/nabil-invest/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_nea_post(self):
        """Test case for api_servicegroup_commit_nea_post

        
        """
        body = Body11()
        response = self.client.open(
            '/api/servicegroup/commit/nea/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_neco_insurance_post(self):
        """Test case for api_servicegroup_commit_neco_insurance_post

        
        """
        body = Body34()
        response = self.client.open(
            '/api/servicegroup/commit/neco-insurance/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_reliance_insurance_post(self):
        """Test case for api_servicegroup_commit_reliance_insurance_post

        
        """
        body = Body40()
        response = self.client.open(
            '/api/servicegroup/commit/reliance-insurance/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_techminds_post(self):
        """Test case for api_servicegroup_commit_techminds_post

        
        """
        body = Body28()
        response = self.client.open(
            '/api/servicegroup/commit/techminds/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_vianet_post(self):
        """Test case for api_servicegroup_commit_vianet_post

        
        """
        body = Body20()
        response = self.client.open(
            '/api/servicegroup/commit/vianet/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_websurfer_post(self):
        """Test case for api_servicegroup_commit_websurfer_post

        SKY CABLE TV AND TOPUP
        """
        body = Body26()
        response = self.client.open(
            '/api/servicegroup/commit/websurfer/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_commit_worldlink_post(self):
        """Test case for api_servicegroup_commit_worldlink_post

        
        """
        body = Body18()
        response = self.client.open(
            '/api/servicegroup/commit/worldlink/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_counters_khanepani_post(self):
        """Test case for api_servicegroup_counters_khanepani_post

        
        """
        body = Body12()
        response = self.client.open(
            '/api/servicegroup/counters/khanepani/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_counters_nea_post(self):
        """Test case for api_servicegroup_counters_nea_post

        
        """
        body = Body8()
        response = self.client.open(
            '/api/servicegroup/counters/nea/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_details_arhant_insurances_post(self):
        """Test case for api_servicegroup_details_arhant_insurances_post

        
        """
        body = Body37()
        response = self.client.open(
            '/api/servicegroup/details/arhant-insurances/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_details_arrownet_post(self):
        """Test case for api_servicegroup_details_arrownet_post

        
        """
        body = Body23()
        response = self.client.open(
            '/api/servicegroup/details/arrownet/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_details_classitech_post(self):
        """Test case for api_servicegroup_details_classitech_post

        
        """
        body = Body21()
        response = self.client.open(
            '/api/servicegroup/details/classitech/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_details_khanepani_post(self):
        """Test case for api_servicegroup_details_khanepani_post

        
        """
        body = Body13()
        response = self.client.open(
            '/api/servicegroup/details/khanepani/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_details_merotv_post(self):
        """Test case for api_servicegroup_details_merotv_post

        
        """
        body = Body15()
        response = self.client.open(
            '/api/servicegroup/details/merotv/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_details_nabil_invest_post(self):
        """Test case for api_servicegroup_details_nabil_invest_post

        
        """
        body = Body41()
        response = self.client.open(
            '/api/servicegroup/details/nabil-invest/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_details_nea_post(self):
        """Test case for api_servicegroup_details_nea_post

        
        """
        body = Body9()
        response = self.client.open(
            '/api/servicegroup/details/nea/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_details_neco_insurance_post(self):
        """Test case for api_servicegroup_details_neco_insurance_post

        
        """
        body = Body33()
        response = self.client.open(
            '/api/servicegroup/details/neco-insurance/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_details_reliance_insurance_post(self):
        """Test case for api_servicegroup_details_reliance_insurance_post

        
        """
        body = Body39()
        response = self.client.open(
            '/api/servicegroup/details/reliance-insurance/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_details_techminds_post(self):
        """Test case for api_servicegroup_details_techminds_post

        
        """
        body = Body27()
        response = self.client.open(
            '/api/servicegroup/details/techminds/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_details_vianet_post(self):
        """Test case for api_servicegroup_details_vianet_post

        
        """
        body = Body19()
        response = self.client.open(
            '/api/servicegroup/details/vianet/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_details_websurfer_post(self):
        """Test case for api_servicegroup_details_websurfer_post

        SKY CABLE TV AND TOPUP
        """
        body = Body25()
        response = self.client.open(
            '/api/servicegroup/details/websurfer/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_details_worldlink_post(self):
        """Test case for api_servicegroup_details_worldlink_post

        
        """
        body = Body17()
        response = self.client.open(
            '/api/servicegroup/details/worldlink/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_downloadticket_movie_post(self):
        """Test case for api_servicegroup_downloadticket_movie_post

        
        """
        body = Body54()
        response = self.client.open(
            '/api/servicegroup/downloadticket/movie/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_getpackagerates_midas_post(self):
        """Test case for api_servicegroup_getpackagerates_midas_post

        MIDAS PACKAGE RATE API
        """
        body = Body30()
        response = self.client.open(
            '/api/servicegroup/getpackagerates/midas/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_getpackages_midas_post(self):
        """Test case for api_servicegroup_getpackages_midas_post

        Midas Package Listing API
        """
        body = Body29()
        response = self.client.open(
            '/api/servicegroup/getpackages/midas/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_issue_flight_post(self):
        """Test case for api_servicegroup_issue_flight_post

        
        """
        body = Body46()
        response = self.client.open(
            '/api/servicegroup/issue/flight/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_search_flight_get(self):
        """Test case for api_servicegroup_search_flight_get

        
        """
        query_string = [('token', 'token_example'),
                        ('reference', 'reference_example'),
                        ('flight_type', 'flight_type_example'),
                        ('trip_type', 'trip_type_example'),
                        ('flight_date', 'flight_date_example'),
                        ('return_date', 'return_date_example'),
                        ('nationality', 'nationality_example'),
                        ('adult', 56),
                        ('child', 56),
                        ('infant', 56),
                        ('_from', '_from_example'),
                        ('to', 'to_example')]
        response = self.client.open(
            '/api/servicegroup/search/flight/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_search_hotel_get(self):
        """Test case for api_servicegroup_search_hotel_get

        
        """
        query_string = [('token', 'token_example'),
                        ('reference', 'reference_example'),
                        ('rooms', 56),
                        ('checkin_date', 'checkin_date_example'),
                        ('checkout_date', 'checkout_date_example'),
                        ('adult', 56),
                        ('child', 56),
                        ('city', 'city_example')]
        response = self.client.open(
            '/api/servicegroup/search/hotel/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_search_midas_get(self):
        """Test case for api_servicegroup_search_midas_get

        
        """
        query_string = [('token', 'token_example'),
                        ('number', 'number_example'),
                        ('reference', 'reference_example')]
        response = self.client.open(
            '/api/servicegroup/search/midas/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_search_movie_get(self):
        """Test case for api_servicegroup_search_movie_get

        
        """
        query_string = [('token', 'token_example')]
        response = self.client.open(
            '/api/servicegroup/search/movie/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_seatsinfo_movie_post(self):
        """Test case for api_servicegroup_seatsinfo_movie_post

        
        """
        body = Body49()
        response = self.client.open(
            '/api/servicegroup/seatsinfo/movie/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_sectors_flight_post(self):
        """Test case for api_servicegroup_sectors_flight_post

        
        """
        body = Body43()
        response = self.client.open(
            '/api/servicegroup/sectors/flight/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_selectseat_movie_post(self):
        """Test case for api_servicegroup_selectseat_movie_post

        
        """
        body = Body50()
        response = self.client.open(
            '/api/servicegroup/selectseat/movie/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_servicecharge_nea_post(self):
        """Test case for api_servicegroup_servicecharge_nea_post

        
        """
        body = Body10()
        response = self.client.open(
            '/api/servicegroup/servicecharge/nea/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_showinfo_movie_post(self):
        """Test case for api_servicegroup_showinfo_movie_post

        
        """
        body = Body48()
        response = self.client.open(
            '/api/servicegroup/showinfo/movie/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroup_unselectseat_movie_post(self):
        """Test case for api_servicegroup_unselectseat_movie_post

        
        """
        body = Body51()
        response = self.client.open(
            '/api/servicegroup/unselectseat/movie/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroups_commit_sagarmatha_insurance_post(self):
        """Test case for api_servicegroups_commit_sagarmatha_insurance_post

        
        """
        body = Body36()
        response = self.client.open(
            '/api/servicegroups/commit/sagarmatha-insurance/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_servicegroups_details_sagarmatha_insurance_post(self):
        """Test case for api_servicegroups_details_sagarmatha_insurance_post

        
        """
        body = Body35()
        response = self.client.open(
            '/api/servicegroups/details/sagarmatha-insurance/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_dishhome_post(self):
        """Test case for api_use_dishhome_post

        
        """
        body = Body14()
        response = self.client.open(
            '/api/use/dishhome/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_use_kaspersky_post(self):
        """Test case for api_use_kaspersky_post

        
        """
        body = Body32()
        response = self.client.open(
            '/api/use/kaspersky/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
