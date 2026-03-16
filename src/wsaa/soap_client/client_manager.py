import httpx
from zeep import AsyncClient
from zeep.transports import AsyncTransport


def wsaa_client(afip_wsdl):
    httpx_client = httpx.AsyncClient(timeout=30.0)
    transport = AsyncTransport(client=httpx_client)
    client = AsyncClient(wsdl=afip_wsdl, transport=transport)

    return client, httpx_client