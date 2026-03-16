from src.shared.paths_config.paths import get_as_bytes
from src.shared.utils.logger import logger
from src.wsaa.crypto.sign import sign_login_ticket_request
from src.wsaa.soap_client.client_manager import wsaa_client
from src.wsaa.soap_client.wsaa import consult_afip_wsaa
from src.wsaa.soap_client.wsdl.wsdl_manager import get_wsaa_wsdl
from src.wsaa.time.time_management import generate_ntp_timestamp
from src.wsaa.xml_management.xml_builder import (
    build_login_ticket_request, parse_and_save_loginticketresponse, save_xml)


async def generate_afip_access_token() -> dict:

    logger.info("Generating a new access token...")

    root = build_login_ticket_request(generate_ntp_timestamp)
    save_xml(root, "loginTicketRequest.xml")
    login_ticket_request_bytes, private_key_bytes, certificate_bytes = get_as_bytes()
    b64_cms = sign_login_ticket_request(login_ticket_request_bytes, private_key_bytes, certificate_bytes)

    afip_wsdl = get_wsaa_wsdl()
    client, httpx_client = wsaa_client(afip_wsdl)

    async def login_cms():
        try:
            return await client.service.loginCms(b64_cms)

        finally:
            if client and client.transport:
                await client.transport.aclose()
            else:
                await httpx_client.aclose()

    login_ticket_response = await consult_afip_wsaa(login_cms, "loginCms")

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
