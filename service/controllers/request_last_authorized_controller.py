from service.payload_builder.builder import (build_auth, extract_cbtenro,
                                             extract_ptovta_and_cbtetipo,
                                             update_sale_data)
from service.soap_client.wsfe import fe_comp_ultimo_autorizado, fecae_solicitar
from service.utils.logger import logger
from service.xml_management.xml_builder import extract_token_and_sign_from_xml


def sync_invoice_number(invoice_info: dict) -> dict:
    logger.info("Starting invoice number synchronization.")

    token, sign = extract_token_and_sign_from_xml("loginTicketResponse.xml")
    cuit, ptovta, cbtetipo = extract_ptovta_and_cbtetipo(invoice_info)
    auth = build_auth(token, sign, cuit)

    last_authorized_invoice = fe_comp_ultimo_autorizado(auth, ptovta, cbtetipo)
    
    return last_authorized_invoice