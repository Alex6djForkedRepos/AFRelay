
# Flag to select WSAA environment:
# True = production, False = testing (homologation)
IS_WSAA_PRODUCTION = False

def get_wsaa_url() -> str:
    if IS_WSAA_PRODUCTION:
        return "https://wsaa.afip.gov.ar/ws/services/LoginCms"
    else:
        return "https://wsaahomo.afip.gov.ar/ws/services/LoginCms"
