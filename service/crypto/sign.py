import base64

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.serialization import pkcs7

from service.utils.logger import logger


def sign_login_ticket_request(
                            login_ticket_request_bytes: bytes, 
                            private_key_bytes: bytes, 
                            certificate_bytes: bytes
                        ) -> str:

    logger.debug("Signing loginTicketRequest.xml...")

    private_key = serialization.load_pem_private_key(private_key_bytes, password=None)
    certificate = x509.load_pem_x509_certificate(certificate_bytes)

    cms_signature = (
        pkcs7.PKCS7SignatureBuilder()
        .set_data(login_ticket_request_bytes)
        .add_signer(certificate, private_key, hashes.SHA256())
        .sign(encoding=serialization.Encoding.DER, options=[])
    )

    b64_cms = base64.b64encode(cms_signature).decode("ascii")
    logger.debug("loginTicketRequest.xml successfully signed.")

    return b64_cms