import connexion
import six

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
from swagger_server import util


def api_download_id_get(id, token, is_base64=None):  # noqa: E501
    """api_download_id_get

    Search FLight  # noqa: E501

    :param id: Enter id.
    :type id: str
    :param token: Enter your token.
    :type token: str
    :param is_base64: If \&quot;True\&quot; return base64 encoded data. (Optinal)
    :type is_base64: str

    :rtype: None
    """
    return 'do some magic!'


def api_lookup_dishhome_get(token, casid):  # noqa: E501
    """api_lookup_dishhome_get

    Customer / CAS ID details  # noqa: E501

    :param token: Please enter your token
    :type token: str
    :param casid: Enter consumer cas id.
    :type casid: str

    :rtype: object
    """
    return 'do some magic!'


def api_products_kaspersky_get(token):  # noqa: E501
    """api_products_kaspersky_get

    Details for Kaspersky.  # noqa: E501

    :param token: Please enter your token
    :type token: str

    :rtype: object
    """
    return 'do some magic!'


def api_servicegroup_addinfo_flight_post(body):  # noqa: E501
    """api_servicegroup_addinfo_flight_post

    Add passenger details for FLight  Booking_id &#x3D; value of booking_id from search response  &lt;br&gt; type &#x3D;  ADULT, CHILD or INFANT &lt;br&gt; title &#x3D; MR, MRS or MS, &lt;br&gt; gender &#x3D; M or F  &lt;br&gt;  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body45.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_book_flight_post(body):  # noqa: E501
    """api_servicegroup_book_flight_post

    Details of FLight  Flight id &#x3D; one of the flight_ids from search response in/outbound list &lt;br&gt; Booking_id &#x3D; value of booking_id from search response  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body44.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_cancel_flight_post(body):  # noqa: E501
    """api_servicegroup_cancel_flight_post

    Payment of FLight  cancel_tickets &#x3D;[\&quot;ticketnumber\&quot;] #Separate by comma for multiple tickets Booking_id &#x3D; value of booking_id from search response  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body47.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_cancel_movie_post(body):  # noqa: E501
    """api_servicegroup_cancel_movie_post

    To cancel all the seats.  session_id &#x3D; value obtained during seatsinfo step  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body52.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_arhant_insurances_post(body):  # noqa: E501
    """api_servicegroup_commit_arhant_insurances_post

    Payment of Insurance Plan.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body38.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_arrownet_post(body):  # noqa: E501
    """api_servicegroup_commit_arrownet_post

    Payment for arrownet.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body24.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_classitech_post(body):  # noqa: E501
    """api_servicegroup_commit_classitech_post

    Payment for Classictech.  session_id &gt; “session id from detail step” &lt;br&gt; amount &gt; “amount from details step” &lt;br&gt; month &gt; “select month from detail step” &lt;br&gt; package &gt; “select package from previous step” &lt;br&gt;  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body22.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_merotv_post(body):  # noqa: E501
    """api_servicegroup_commit_merotv_post

    MeroTv Payment.  “session_id” &gt; “session_id return during detail step”  “package_id” &gt; “&lt;package_id from details step&gt;”  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body16.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_midas_post(body):  # noqa: E501
    """api_servicegroup_commit_midas_post

    Payment for Midas.  ‘session_id&#x27; &#x3D; ‘&lt;session_id returned during seatch step&gt;’, &lt;br&gt; “package_code” &#x3D; “package code from previous step”  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body31.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_movie_post(body):  # noqa: E501
    """api_servicegroup_commit_movie_post

    Payment for the movie.  session_id &#x3D; value obtained during seatsinfo step  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body53.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_nabil_invest_post(body):  # noqa: E501
    """api_servicegroup_commit_nabil_invest_post

    Payment of Insurance Plan.  “session_id” &#x3D; “session_id from previous step”,  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body42.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_nea_post(body):  # noqa: E501
    """api_servicegroup_commit_nea_post

    Payment for Nea.   session_id &#x3D; value obtained during customer detail  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body11.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_neco_insurance_post(body):  # noqa: E501
    """api_servicegroup_commit_neco_insurance_post

    Payment of Insurance Plan.  \&quot;insurance_slug\&quot; &#x3D; \&quot;neco-insurance\&quot; &lt;br&gt; ‘policy_type’ &#x3D; Fresh OR Renew      &lt;br&gt; ‘policy_category’ &#x3D; Any one value from categories above   &lt;br&gt; ‘reference_identifier’ &#x3D; unique identifier for each request &lt;br&gt; ‘service_name’ &#x3D; ‘neco-insurance’,  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body34.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_reliance_insurance_post(body):  # noqa: E501
    """api_servicegroup_commit_reliance_insurance_post

    Payment of Insurance Plan.  “transaction_id” &#x3D; “transaction id from details step”,  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body40.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_techminds_post(body):  # noqa: E501
    """api_servicegroup_commit_techminds_post

    Payment for Techmind.  ‘session_id&#x27; &#x3D; ‘&lt;session_id returned during user lookup&gt;’, &lt;br&gt;  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body28.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_vianet_post(body):  # noqa: E501
    """api_servicegroup_commit_vianet_post

    Payment for Vianet.  session_id &#x3D; &lt;Session id, as obtained in details step&gt; &lt;br&gt; customer_id &#x3D; &lt;Customer Id, same as in details step&gt;  &lt;br&gt; payment_id &#x3D; &lt;Payment Id, as obtained in details step&gt; &lt;br&gt;  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body20.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_websurfer_post(body):  # noqa: E501
    """SKY CABLE TV AND TOPUP

    Payment for Sky tv and Internet.  ‘session_id&#x27; &#x3D; ‘&lt;session_id returned during user lookup&gt;’, &lt;br&gt; ‘code’ &#x3D; ‘&lt;code associated with the package (see in User lookup Response)&gt;’, &lt;br&gt; ‘service’ &#x3D; ‘sky-tv (For TV) / sky-internet (For Internet)’  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body26.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_commit_worldlink_post(body):  # noqa: E501
    """api_servicegroup_commit_worldlink_post

    Payment for worldlink.  payment_type &#x3D; &lt;’Advanced’ or ‘Normal’&gt;,  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body18.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_counters_khanepani_post(body):  # noqa: E501
    """api_servicegroup_counters_khanepani_post

    Details of Khanepani counters # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body12.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_counters_nea_post(body):  # noqa: E501
    """api_servicegroup_counters_nea_post

    Details of electricity counters # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body8.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_details_arhant_insurances_post(body):  # noqa: E501
    """api_servicegroup_details_arhant_insurances_post

    Details of Insurance Plan.  Note &#x3D; Below is the list of Insurances under Arhant and their insurance_slug  Premier Insurance &#x3D; premier-insurance (TEST now only available for this) Prudential Insurance &#x3D; prudential-insurance United Insurance &#x3D; united-insurance National Insurance &#x3D; national-insurance NLG Insurance &#x3D; nlg-insurance   …..others to be added  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body37.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_details_arrownet_post(body):  # noqa: E501
    """api_servicegroup_details_arrownet_post

    Details for arrownet.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body23.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_details_classitech_post(body):  # noqa: E501
    """api_servicegroup_details_classitech_post

    Payment details for classictech.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body21.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_details_khanepani_post(body):  # noqa: E501
    """api_servicegroup_details_khanepani_post

    Details of customer.  counter &#x3D; &lt; one of the ‘value’ fields from Counter detail &gt;  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body13.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_details_merotv_post(body):  # noqa: E501
    """api_servicegroup_details_merotv_post

    Details of merotv client  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body15.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_details_nabil_invest_post(body):  # noqa: E501
    """api_servicegroup_details_nabil_invest_post

    Payment of Insurance Plan.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body41.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_details_nea_post(body):  # noqa: E501
    """api_servicegroup_details_nea_post

    Details of customer.  office code &#x3D; one of the ’value’ fields of the response from counters  details  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body9.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_details_neco_insurance_post(body):  # noqa: E501
    """api_servicegroup_details_neco_insurance_post

    Details of Insurance Plan.  \&quot;insurance_slug\&quot; &#x3D; \&quot;neco-insurance\&quot;  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body33.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_details_reliance_insurance_post(body):  # noqa: E501
    """api_servicegroup_details_reliance_insurance_post

    Detail of Insurance Plan.  “dob” &#x3D; “YYYY-MM-DD”  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body39.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_details_techminds_post(body):  # noqa: E501
    """api_servicegroup_details_techminds_post

    Details for Techmind.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body27.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_details_vianet_post(body):  # noqa: E501
    """api_servicegroup_details_vianet_post

    Details of Vianet  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body19.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_details_websurfer_post(body):  # noqa: E501
    """SKY CABLE TV AND TOPUP

    Details for Skytv and Internet. stb/username &#x3D; Unique setupbox number/ username &lt;br&gt; ‘service’ &#x3D; ‘sky-tv (For TV) / sky-internet (For Internet)’  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body25.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_details_worldlink_post(body):  # noqa: E501
    """api_servicegroup_details_worldlink_post

    Details of Worldlink.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body17.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_downloadticket_movie_post(body):  # noqa: E501
    """api_servicegroup_downloadticket_movie_post

    Download ticket.  session_id &#x3D; value obtained during seatsinfo step  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body54.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_getpackagerates_midas_post(body):  # noqa: E501
    """MIDAS PACKAGE RATE API

    Package Rate for Midas.  ‘session_id&#x27; &#x3D; ‘&lt;session_id returned during seatch step&gt;’, &lt;br&gt; “package_id” &#x3D; “the id of package from previous step”, &lt;br&gt; “number_of_days” &#x3D; “number of days from previous step”  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body30.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_getpackages_midas_post(body):  # noqa: E501
    """Midas Package Listing API

    Packet Listing for Midas.  ‘session_id&#x27; &#x3D; ‘&lt;session_id returned during seatch step&gt;’, &lt;br&gt;  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body29.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_issue_flight_post(body):  # noqa: E501
    """api_servicegroup_issue_flight_post

    Payment of FLight  Flight id &#x3D; one of the flight_ids from search response in/outbound list &lt;br&gt; Booking_id &#x3D; value of booking_id from search response  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body46.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_search_flight_get(token, reference, flight_type, trip_type, flight_date, nationality, adult, _from, to, return_date=None, child=None, infant=None):  # noqa: E501
    """api_servicegroup_search_flight_get

    Search FLight  # noqa: E501

    :param token: Enter your token.
    :type token: str
    :param reference: Reference must be unique
    :type reference: str
    :param flight_type: One of the flight type ‘D’ for domestic and ‘I’ for international. (mandatory).
    :type flight_type: str
    :param trip_type: One of the trip type  ‘O’ for one way and ‘R’ for return. (mandatory).
    :type trip_type: str
    :param flight_date: YYYY-MM-DD (mandatory).
    :type flight_date: str
    :param nationality: Country code of the passenger(NP for Nepal)
    :type nationality: str
    :param adult: Number of Adults.
    :type adult: int
    :param _from: Origin Sector code explained below, e.g. ‘PKR’  for Pokhara
    :type _from: str
    :param to: Destination Sector code
    :type to: str
    :param return_date: YYYY-MM-DD
    :type return_date: str
    :param child: Number of Children.
    :type child: int
    :param infant: Number of Infant
    :type infant: int

    :rtype: None
    """
    return 'do some magic!'


def api_servicegroup_search_hotel_get(token, reference, rooms, checkin_date, checkout_date, adult, city, child=None):  # noqa: E501
    """api_servicegroup_search_hotel_get

    Search Hotel  session_id &#x3D; value obtained during seatsinfo step  # noqa: E501

    :param token: Enter your token.
    :type token: str
    :param reference: Reference must be unique
    :type reference: str
    :param rooms: Number of rooms.
    :type rooms: int
    :param checkin_date: YYYY-MM-DD
    :type checkin_date: str
    :param checkout_date: YYYY-MM-DD
    :type checkout_date: str
    :param adult: Number of Adults.
    :type adult: int
    :param city: Name of city.
    :type city: str
    :param child: Number of Children.
    :type child: int

    :rtype: None
    """
    return 'do some magic!'


def api_servicegroup_search_midas_get(token, number, reference):  # noqa: E501
    """api_servicegroup_search_midas_get

    Details for Midas.  # noqa: E501

    :param token: Please enter your token
    :type token: str
    :param number: Enter your number.
    :type number: str
    :param reference: Reference must be unique
    :type reference: str

    :rtype: object
    """
    return 'do some magic!'


def api_servicegroup_search_movie_get(token):  # noqa: E501
    """api_servicegroup_search_movie_get

    Search FLight  # noqa: E501

    :param token: Enter your token.
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def api_servicegroup_seatsinfo_movie_post(body):  # noqa: E501
    """api_servicegroup_seatsinfo_movie_post

    Movie seat information.    show_id &#x3D; one of the show_id values obtained in search &lt;br&gt; ticket_type_id &#x3D; ticket_type_id values obtained in showinfo &lt;br&gt; old_session_id &#x3D; leave it empty or set some value. Read NOTE that follows  NOTE This api will return a new session_id if ‘old_session’ is not set.  If set, this will not returnnew session_id and is used for changing the price levels of the auditorim &lt;br&gt; Example Auditorium 1 of a theatre can have ‘Gold seats’ and ‘Premium seats’, setting old_session will allow switching between the seats without creating new session.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body49.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_sectors_flight_post(body):  # noqa: E501
    """api_servicegroup_sectors_flight_post

    Details of FLight  “session_id” &#x3D; “session_id from previous step”,  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body43.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_selectseat_movie_post(body):  # noqa: E501
    """api_servicegroup_selectseat_movie_post

    To select seat.  seat_id &#x3D;  seat_id of the seat to be unselected &lt;br&gt; session_id &#x3D; value obtained during seatsinfo step  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body50.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_servicecharge_nea_post(body):  # noqa: E501
    """api_servicegroup_servicecharge_nea_post

    Get service charge Nea.   session_id &#x3D; value obtained during customer detail  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body10.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_showinfo_movie_post(body):  # noqa: E501
    """api_servicegroup_showinfo_movie_post

    Movie show information.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body48.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroup_unselectseat_movie_post(body):  # noqa: E501
    """api_servicegroup_unselectseat_movie_post

    To unselect seat.  seat_id &#x3D;  seat_id of the seat to be unselected &lt;br&gt; session_id &#x3D; value obtained during seatsinfo step  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body51.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroups_commit_sagarmatha_insurance_post(body):  # noqa: E501
    """api_servicegroups_commit_sagarmatha_insurance_post

    Payment of Insurance Plan.  session_id &#x3D; session_id returned during user lookup  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body36.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_servicegroups_details_sagarmatha_insurance_post(body):  # noqa: E501
    """api_servicegroups_details_sagarmatha_insurance_post

    Details of Insurance Plan.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body35.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_dishhome_post(body):  # noqa: E501
    """api_use_dishhome_post

    Lets a user make payment for Dishhome. &lt;br&gt; Valid Amounts 300, 350, 400, 500, 600, 700, 1000, 2000, 3000, 4000, 5000, 6000, 7000  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body14.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_kaspersky_post(body):  # noqa: E501
    """api_use_kaspersky_post

    Payment for Kaspersky.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body32.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
