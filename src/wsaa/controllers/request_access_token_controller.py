from src.shared.paths_config.paths import get_as_bytes
from src.shared.utils.logger import logger
from src.wsaa.crypto.sign import sign_login_ticket_request
from src.wsaa.soap_client.wsaa import consult_afip_wsaa
from src.wsaa.time.time_management import generate_ntp_timestamp
from src.wsaa.xml_management.xml_builder import (
    build_login_ticket_request, build_xml_to_send,
    parse_and_save_loginticketresponse, save_xml)


async def generate_afip_access_token() -> dict:

    logger.info("Generating a new access token...")

    root = build_login_ticket_request(generate_ntp_timestamp)
    save_xml(root, "loginTicketRequest.xml")
    login_ticket_request_bytes, private_key_bytes, certificate_bytes = get_as_bytes()
    b64_cms = sign_login_ticket_request(login_ticket_request_bytes, private_key_bytes, certificate_bytes)
    wsaa_xml = build_xml_to_send(b64_cms)

    login_ticket_response = await consult_afip_wsaa(wsaa_xml)

    if login_ticket_response["status"] == "success":
        parse_and_save_loginticketresponse(login_ticket_response["response"], save_xml)
    
        logger.info("Token generated successfully.")
        return {
            "status" : "success"
            }

    else:
        logger.error("Failed to generate access token.")
        return {
            "status" : "error generating access token."
            }
