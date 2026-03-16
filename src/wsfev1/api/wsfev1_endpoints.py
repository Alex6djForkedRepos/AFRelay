from fastapi import APIRouter, Depends

from src.shared.api.jwt_validator import verify_token
from src.shared.utils.logger import logger
from src.wsfev1.api.request_models.fe_comp_consultar import FECompConsultar
from src.wsfev1.api.request_models.fecae_solicitar import FECAESolicitar
from src.wsfev1.api.request_models.fecaea_reg_informativo import \
    FECAEARegInformativo
from src.wsfev1.api.request_models.simple_models import (
    FECAEAConsultar, FECAEASinMovimientoConsultar, FECAEASinMovimientoInformar,
    FECAEASolicitar, FECompTotXRequest, FECompUltimoAutorizado,
    FEParamGetActividades, FEParamGetCondicionIvaReceptor,
    FEParamGetCotizacion, FEParamGetPtosVenta, FEParamGetTiposCbte,
    FEParamGetTiposConcepto, FEParamGetTiposDoc, FEParamGetTiposIva,
    FEParamGetTiposMonedas, FEParamGetTiposOpcional, FEParamGetTiposPaises,
    FEParamGetTiposTributos)
from src.wsfev1.api.response_models import simple_models
from src.wsfev1.api.response_models.common import APIErrorResponseModel
from src.wsfev1.api.response_models.fe_comp_consultar import \
    FECompConsultarResponse
from src.wsfev1.api.response_models.fecae_solicitar import \
    FECAESolicitarResponse
from src.wsfev1.api.response_models.fecaea_reg_informativo import \
    FECAEARegInformativoResponse
from src.wsfev1.payload_builder.builder import add_auth_to_payload
from src.wsfev1.soap_client.client_manager import WSFEClientManager
from src.wsfev1.soap_client.wsdl.wsdl_manager import get_wsfe_wsdl
from src.wsfev1.soap_client.wsfev1 import consult_afip_wsfe
from src.wsfev1.xml_management.xml_builder import \
    extract_token_and_sign_from_xml

router = APIRouter()
afip_wsdl = get_wsfe_wsdl()


@router.post("/wsfev1/FECAESolicitar", response_model=FECAESolicitarResponse | APIErrorResponseModel)
async def fecae_solicitar(data: FECAESolicitar, jwt = Depends(verify_token)) -> dict:
    
    logger.info("Received request to generate invoice at /wsfe/FECAESolicitar")

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECAESolicitar(**data)

    result = await consult_afip_wsfe(make_request, "FECAESolicitar")
    return result


@router.post("/wsfev1/FECompTotXRequest", response_model = simple_models.FECompTotXRequestResponse | APIErrorResponseModel)
async def fecomp_totx_request(data: FECompTotXRequest, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECompTotXRequest(**data)
    
    result = await consult_afip_wsfe(make_request, "FECompTotXRequest")
    return result


@router.post("/wsfev1/FECompUltimoAutorizado", response_model = simple_models.FECompUltimoAutorizadoResponse | APIErrorResponseModel)
async def fe_comp_ultimo_autorizado(data: FECompUltimoAutorizado, jwt = Depends(verify_token)) -> dict:
    logger.info("Received request to generate invoice at /wsfe/FECompUltimoAutorizado")

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECompUltimoAutorizado(**data)

    result = await consult_afip_wsfe(make_request, "FECompUltimoAutorizado")
    return result


@router.post("/wsfev1/FECompConsultar", response_model=FECompConsultarResponse | APIErrorResponseModel)
async def fe_comp_consultar(comp_info: FECompConsultar, jwt = Depends(verify_token)) -> dict:
    logger.info("Received request to query specific invoice at /wsfe/FECompConsultar")

    data = comp_info.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECompConsultar(**data)

    result = await consult_afip_wsfe(make_request, "FECompConsultar")
    return result


@router.post("/wsfev1/FECAEARegInformativo", response_model=FECAEARegInformativoResponse | APIErrorResponseModel)
async def fecaea_reg_informativo(data: FECAEARegInformativo, jwt = Depends(verify_token)) -> dict:
    
    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECAEARegInformativo(**data)

    result = await consult_afip_wsfe(make_request, "FECAEARegInformativo")
    return result


@router.post("/wsfev1/FECAEASolicitar", response_model = simple_models.FECAEASolicitarResponse | APIErrorResponseModel)
async def fecaea_solicitar(data: FECAEASolicitar, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECAEASolicitar(**data)
    
    result = await consult_afip_wsfe(make_request, "FECAEASolicitar")
    return result


@router.post("/wsfev1/FECAEASinMovimientoConsultar", response_model = simple_models.FECAEASinMovimientoConsultarResponse | APIErrorResponseModel)
async def fecaea_sin_movimiento_consultar(data: FECAEASinMovimientoConsultar, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECAEASinMovimientoConsultar(**data)
    
    result = await consult_afip_wsfe(make_request, "FECAEASinMovimientoConsultar")
    return result


@router.post("/wsfev1/FECAEASinMovimientoInformar", response_model = simple_models.FECAEASinMovimientoInformarResponse | APIErrorResponseModel)
async def fecaea_sin_movimiento_informar(data: FECAEASinMovimientoInformar, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECAEASinMovimientoInformar(**data)
    
    result = await consult_afip_wsfe(make_request, "FECAEASinMovimientoInformar")
    return result


@router.post("/wsfev1/FECAEAConsultar", response_model = simple_models.FECAEAConsultarResponse | APIErrorResponseModel)
async def fecaea_consultar(data: FECAEAConsultar, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FECAEAConsultar(**data)
    
    result = await consult_afip_wsfe(make_request, "FECAEAConsultar")
    return result


@router.post("/wsfev1/FEParamGetCotizacion", response_model = simple_models.FEParamGetCotizacionResponse | APIErrorResponseModel)
async def fe_param_get_cotization(data: FEParamGetCotizacion, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetCotizacion(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetCotizacion")
    return result


@router.post("/wsfev1/FEParamGetTiposTributos", response_model = simple_models.FEParamGetTiposTributosResponse | APIErrorResponseModel)
async def fe_param_get_tipos_tributos(data: FEParamGetTiposTributos, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposTributos(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposTributos")
    return result


@router.post("/wsfev1/FEParamGetTiposMonedas", response_model = simple_models.FEParamGetTiposMonedasResponse | APIErrorResponseModel)
async def fe_param_get_tipos_monedas(data: FEParamGetTiposMonedas, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposMonedas(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposMonedas")
    return result


@router.post("/wsfev1/FEParamGetTiposIva", response_model = simple_models.FEParamGetTiposIvaResponse | APIErrorResponseModel)
async def fe_param_get_tipos_iva(data: FEParamGetTiposIva, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposIva(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposIva")
    return result


@router.post("/wsfev1/FEParamGetTiposOpcional", response_model = simple_models.FEParamGetTiposOpcionalResponse | APIErrorResponseModel)
async def fe_param_get_tipos_opcional(data: FEParamGetTiposOpcional, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposOpcional(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposOpcional")
    return result


@router.post("/wsfev1/FEParamGetTiposConcepto", response_model = simple_models.FEParamGetTiposConceptoResponse | APIErrorResponseModel)
async def fe_param_get_tipos_concepto(data: FEParamGetTiposConcepto, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposConcepto(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposConcepto")
    return result


@router.post("/wsfev1/FEParamGetPtosVenta", response_model = simple_models.FEParamGetPtosVentaResponse | APIErrorResponseModel)
async def fe_param_get_ptos_venta(data: FEParamGetPtosVenta, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetPtosVenta(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetPtosVenta")
    return result


@router.post("/wsfev1/FEParamGetTiposCbte", response_model = simple_models.FEParamGetTiposCbteResponse | APIErrorResponseModel)
async def fe_param_get_tipos_cbte(data: FEParamGetTiposCbte, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposCbte(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposCbte")
    return result


@router.post("/wsfev1/FEParamGetCondicionIvaReceptor", response_model = simple_models.FEParamGetCondicionIvaReceptorResponse | APIErrorResponseModel)
async def fe_param_get_condicion_iva_receptor(data: FEParamGetCondicionIvaReceptor, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetCondicionIvaReceptor(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetCondicionIvaReceptor")
    return result


@router.post("/wsfev1/FEParamGetTiposDoc", response_model = simple_models.FEParamGetTiposDocResponse | APIErrorResponseModel)
async def fe_param_get_tipos_doc(data: FEParamGetTiposDoc, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposDoc(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposDoc")
    return result


@router.post("/wsfev1/FEParamGetTiposPaises", response_model = simple_models.FEParamGetTiposPaisesResponse | APIErrorResponseModel)
async def fe_param_get_tipos_paises(data: FEParamGetTiposPaises, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetTiposPaises(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetTiposPaises")
    return result


@router.post("/wsfev1/FEParamGetActividades", response_model = simple_models.FEParamGetActividadesResponse | APIErrorResponseModel)
async def fe_param_get_actividades(data: FEParamGetActividades, jwt = Depends(verify_token)) -> dict:

    data = data.model_dump(by_alias=True, exclude_none=True)
    token, sign = extract_token_and_sign_from_xml()
    data = add_auth_to_payload(data, token, sign)

    async def make_request():
        manager = WSFEClientManager(afip_wsdl)
        client = manager.get_client()
        return await client.service.FEParamGetActividades(**data)
    
    result = await consult_afip_wsfe(make_request, "FEParamGetActividades")
    return result