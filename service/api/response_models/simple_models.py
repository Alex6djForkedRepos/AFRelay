from pydantic import BaseModel, ConfigDict, Field

from service.api.response_models.common import (Errors, Events,
                                                FECAEAGetResponse,
                                                FECAEASinMov)

# ========================================================

class FECompTotXRequestResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    RegXReq: int

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECompTotXRequestResponse(BaseModel):
    status: str
    response: FECompTotXRequestResult

# ========================================================

class FECompUltimoAutorizadoResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    PtoVta: int
    CbteTipo: int
    CbteNro: int | None = None

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECompUltimoAutorizadoResponse(BaseModel):
    status: str
    response: FECompUltimoAutorizadoResult

# ========================================================

class FECAEASinMovimientoConsultarResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    fecaea_sin_mov: list[FECAEASinMov] | None = Field(None, alias="FECAEASinMov")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECAEASinMovimientoConsultarResponse(BaseModel):
    status: str
    response: FECAEASinMovimientoConsultarResult

# ========================================================

class FECAEASinMovimientoInformarResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    fecaea_sin_mov: list[FECAEASinMov] | None = Field(None, alias="FECAEASinMov")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECAEASinMovimientoInformarResponse(BaseModel):
    status: str
    response: FECAEASinMovimientoConsultarResult

# ========================================================

class FECAEAConsultarResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    fecaea_get_response: FECAEAGetResponse | None = Field(None, alias="FECAEAGetResponse")

class FECAEAConsultarResponse(BaseModel):
    status: str 
    response: FECAEAConsultarResult

# ========================================================

class ResultGet(BaseModel):
    MonId: str
    MonCotiz: float
    FchCotiz: str

class FECotizacionResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    errors: Errors | None = Field(None, alias="Errors")
    events: Events | None = Field(None, alias="Events")

class FEParamGetCotizacionResponse(BaseModel):
    status: str   
    response: FECotizacionResult

# ========================================================

class TributoTipo(BaseModel):
    Id: int
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class FEParamGetTiposTributosResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    tributo_tipo: list[TributoTipo] | None = Field(None, alias="TributoTipo")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposTributosResponse(BaseModel):
    status: str
    response: FEParamGetTiposTributosResult

# ========================================================

class Moneda(BaseModel):
    Id: str | None = None
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class FEParamGetTiposMonedasResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    moneda: list[Moneda] | None = Field(None, alias="Moneda")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposMonedasResponse(BaseModel):
    status: str
    response: FEParamGetTiposMonedasResult

# ========================================================

class IvaTipo(BaseModel):
    Id: str | None = None
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class FEParamGetTiposIvaResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    iva_tipo: list[IvaTipo] | None = Field(None, alias="IvaTipo")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposIvaResponse(BaseModel):
    status: str
    response: FEParamGetTiposIvaResult

# ========================================================

class OpcionalTipo(BaseModel):
    Id: str | None = None
    Desc: str | None = None
    FchDesde: str | None = None
    FchHasta: str | None = None

class FEParamGetTiposOpcionalResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    opcional_tipo: list[OpcionalTipo] | None = Field(None, alias="OpcionalTipo")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FEParamGetTiposOpcionalResponse(BaseModel):
    status: str
    response: FEParamGetTiposOpcionalResult