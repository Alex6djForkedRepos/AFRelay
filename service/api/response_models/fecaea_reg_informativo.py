from pydantic import BaseModel, ConfigDict, Field

from service.api.response_models.common import Errors, Events, Observaciones


class Obs(BaseModel):
    Code: int
    Msg: str | None = None


class Observaciones(BaseModel):
    obs: list[Obs] | None = Field(None, alias="Obs")


class FEDetResponse(BaseModel):
    Concepto: int
    DocTipo: int
    DocNro: int
    CbteDesde: int
    CbteHasta: int
    CbteFch: str | None = None
    Resultado: str | None = None

    observaciones: Observaciones | None = Field(None, alias="Observaciones")


class FECAEADetResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    Concepto: int
    DocTipo: int
    DocNro: int
    CbteDesde: int
    CbteHasta: int
    CbteFch: str | None = None
    Resultado: str | None = None
    CAEA: str | None = None

class FECabResponse(BaseModel):
    Cuit: int
    PtoVta: int
    CbteTipo: int
    FchProceso: str | None = None
    CantReg: int
    Resultado: str | None = None
    Reproceso: str | None = None


class FECAEACabResponse(BaseModel):
    Cuit: int
    PtoVta: int
    CbteTipo: int
    FchProceso: str | None = None
    CantReg: int
    Resultado: str | None = None
    Reproceso: str | None = None


class FeDetResp(BaseModel):
    fecae_det_response: list[FECAEADetResponse] | None = Field(None, alias="FECAEADetResponse")


class FeCabResp(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    Cuit: int
    PtoVta: int
    CbteTipo: int
    FchProceso: str | None = None
    CantReg: int
    Resultado: str | None = None
    Reproceso: str | None = None


class FECAEAResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    fe_cab_resp: FeCabResp | None = Field(None, alias="FeCabResp")
    fe_det_resp: FeDetResp | None = Field(None, alias="FeDetResp")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")


class FECAEARegInformativoResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    fecaea_response: FECAEAResponse | None = Field(None, alias="FECAEAResponse")


class FECAEARegInformativoResponse(BaseModel):
    status: str
    response: FECAEARegInformativoResult

