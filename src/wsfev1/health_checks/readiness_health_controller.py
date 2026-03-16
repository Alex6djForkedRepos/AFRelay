import socket

import ntplib
from zeep.helpers import serialize_object

from src.shared.utils.logger import logger
from src.wsfev1.soap_client.wsfev1 import wsfe_dummy


async def readiness_health_check() -> dict:
    logger.debug("Starting readiness health check")
    ntp = ""

    ntp_status = request_ntp_for_readiness()
    if ntp_status:
        ntp = "OK"
        logger.debug("NTP readiness check OK")

    else:
        ntp = {
            "status": "error",
            "message": "NTP query failed",
            "server": "time.afip.gov.ar"
        }
        logger.warning("NTP readiness check FAILED")

    # Check WSFE 
    wsfe_health_info = await wsfe_dummy()

    # Zeep returns an object of type '<class 'zeep.objects.[service response]'>'.
    # To work with the returned data, this object needs to be converted into a dictionary using serialize_object().
    wsfe_health_info_parsed = serialize_object(wsfe_health_info)
    logger.debug("WSFE dummy check OK")

    logger.debug("Readiness health check finished")
    return {
        "ntp" : ntp,
        "wsfe_health" : wsfe_health_info_parsed
        }

def request_ntp_for_readiness() -> bool:
    try:
        logger.debug("Checking NTP availability for readiness...")
        client = ntplib.NTPClient()
        client.request("time.afip.gov.ar", timeout=5)
        return True
    
    except socket.timeout:
        logger.warning("NTP request timed out")
        return False
    
    except Exception as e:
        logger.warning(f"NTP readiness check failed: {e}")
        return False