import connexion
import six

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
from swagger_server import util


def api_use_adsl_ul_post(body):  # noqa: E501
    """api_use_adsl_ul_post

    Lets a user make payment for adsl unlimited. &lt;br&gt; Valid Amounts for both unlimited &amp; volume based \&quot;500, 1000, 1500, 2000, 2500, 3000, 4000, 5000\&quot; &lt;br/&gt; # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Topup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_alisha_communication_post(body):  # noqa: E501
    """api_use_alisha_communication_post

    Lets a user make payment for Alisha Communication. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body4.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_cleartv_post(body):  # noqa: E501
    """api_use_cleartv_post

    ClearTv Payment.     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body2.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_hons_post(body):  # noqa: E501
    """api_use_hons_post

    Lets a user make payment for Hons.  Amount should be greater than or equal to 100  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Network.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_infonet_communication_post(body):  # noqa: E501
    """api_use_infonet_communication_post

    Lets a user make payment for infonet Communication. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body5.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_khalti_topup_post(body):  # noqa: E501
    """api_use_khalti_topup_post

    Lets a user to topup Khalti account # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Topup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_landline_post(body):  # noqa: E501
    """api_use_landline_post

    Lets a user make payment for landline # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Topup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_method_post(body, method):  # noqa: E501
    """api_use_method_post

    Please use the follwing methods \&quot; dishhome-erc, ntc-erc, utl-erc, smart-erc, broadlink-erc \&quot; # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param method: 
    :type method: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_metrolink_post(body):  # noqa: E501
    """api_use_metrolink_post

    Lets a user make payment for metrolink. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body6.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_ncell_post(body):  # noqa: E501
    """api_use_ncell_post

    Lets a user to topup Ncell # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Topup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_ntc_post(body):  # noqa: E501
    """api_use_ntc_post

    Lets a user to topup NTC # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Topup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_pokhara_internet_post(body):  # noqa: E501
    """api_use_pokhara_internet_post

    Lets a user make payment for Pokhara Internet.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body3.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_royal_network_post(body):  # noqa: E501
    """api_use_royal_network_post

    Lets a user make payment for Royal Network.  Amount should be greater than or equal to 100  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Network.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_service_slug_post(body, service_slug):  # noqa: E501
    """Capital Share

    Lets a user make payment for Capital Share.   i) Sunrise Capital API (demat-sunrise/meroshare-sunrise) &lt;br&gt; ii) Laxmi Capital API (demat-laxmi/meroshare-laxmi) &lt;br&gt; iii) BOK Capital API (demat-bok/meroshare-bok)  &lt;br&gt; iv) Sanima Capital API (demat-sanima/meroshare-sanima) &lt;br&gt; v) Prabhu Capital (demat-prabhu/meroshare-prabhu) &lt;br&gt; vi) NIC Asia Capital (demat-nicasia/meroshare-nicasia)  &lt;br&gt;            Note; Choose service_slug from above data. Ex; service_slug of Sunrise Capital Demat is “demat-sunrise”  # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param service_slug: 
    :type service_slug: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body7.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_simtv_post(body):  # noqa: E501
    """api_use_simtv_post

    Lets a user make payment for landline. &lt;br&gt; Use amount from 50 to 50000 &lt;br/&gt; # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_sky_topup_post(body):  # noqa: E501
    """api_use_sky_topup_post

    Lets a user make payment for Sky topup. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Internet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_smartcell_post(body):  # noqa: E501
    """api_use_smartcell_post

    Lets a user to topup Smartcell # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Topup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_subisu_post(body):  # noqa: E501
    """api_use_subisu_post

    Lets a user make payment for Subisu.  Amount should be between 400 and 15000 inclusive  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Internet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_virtual_network_post(body):  # noqa: E501
    """api_use_virtual_network_post

    Lets a user make payment for Virtual Network.  Amount should be greater than or equal to 100  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Network.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_web_network_post(body):  # noqa: E501
    """api_use_web_network_post

    Lets a user make payment for Web Network.  Amount should be greater than or equal to 100  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Network.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_use_websurfer_topup_post(body):  # noqa: E501
    """api_use_websurfer_topup_post

    Lets a user make payment for Websurfer. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Internet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
