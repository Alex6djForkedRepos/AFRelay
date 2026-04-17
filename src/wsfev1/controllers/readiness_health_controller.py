import socket

import ntplib

from src.shared.utils.logger import logger
from src.wsfev1.soap_client import templates
from src.wsfev1.soap_client.wsfev1 import consult_afip_wsfev1


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
    wsfev1_health_info = await consult_afip_wsfev1(templates.FEDummy ,"FEDummy")

    logger.debug("WSFE dummy check OK")

    logger.debug("Readiness health check finished")
    return {
        "ntp" : ntp,
        "wsfe_health" : wsfev1_health_info
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