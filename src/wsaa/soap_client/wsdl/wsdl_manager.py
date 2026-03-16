import os

# Flag to select WSAA environment:
# True = production, False = testing (homologation)
IS_WSAA_PRODUCTION = False
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_wsaa_wsdl() -> str:
    if IS_WSAA_PRODUCTION:
        filename = "wsaa_prod.wsdl"
        return os.path.join(CURRENT_DIR, filename)
    else:
        filename = "wsaa_homo.wsdl"
        return os.path.join(CURRENT_DIR, filename)
