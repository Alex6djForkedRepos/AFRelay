from pydantic import BaseModel

from service.api.models.common import Auth


class FECompTotXRequest(BaseModel):
    Auth: Auth

class FECompUltimoAutorizado(BaseModel):
    Auth: Auth

    PtoVta: int
    CbteTipo: int

class FECAEASolicitar(BaseModel):
    Auth: Auth

    Periodo: int
    Orden: int

class FECAEASinMovimientoConsultar(BaseModel):
    Auth: Auth

    CAEA: str
    PtoVta: int

class FECAEASinMovimientoInformar(BaseModel):
    Auth: Auth

    PtoVta: int
    CAEA: str

class FECAEAConsultar(BaseModel):
    Auth: Auth

    Periodo: int
    Orden: int

class FEParamGetCotizacion(BaseModel):
    Auth: Auth

    MonId: str
    FchCotiz: str | None = None