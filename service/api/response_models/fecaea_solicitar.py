from pydantic import BaseModel, ConfigDict, Field

from service.api.response_models.common import Errors, Events, Observaciones


class ResultGet(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    CAEA: str | None = None
    Periodo: int
    Orden: int
    FchVto: str
    FchVigDesde: str | None = None
    FchVigHasta: str | None = None
    FchLimiteInf: str | None = None
    FchProceso: str | None = None

    observaciones: Observaciones | None = Field(None, alias="Observaciones")

class FECAEASolicitarResult(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    result_get: ResultGet | None = Field(None, alias="ResultGet")

    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECAEASolicitarResponse(BaseModel):
    status: str
    response: FECAEASolicitarResult