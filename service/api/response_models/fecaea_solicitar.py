from pydantic import BaseModel, ConfigDict, Field

from service.api.response_models.common import Errors, Events, Observaciones

class FECAEAGet(BaseModel):
    CAEA: str | None = None
    Periodo: int
    Orden: int
    FchVigDesde: str| None = None
    FchVigHasta: str | None = None
    FchTopeInf: str | None = None
    FchProceso: str | None = None

    observaciones: Observaciones | None = Field(None, alias="Observaciones")


class FECAEASolicitarResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    fecaea_get: FECAEAGet | None = Field(None, alias="FECAEAGet")
    events: Events | None = Field(None, alias="Events")
    errors: Errors | None = Field(None, alias="Errors")

class FECAEASolicitarResponse(BaseModel):
    status: str
    response: FECAEASolicitarResult