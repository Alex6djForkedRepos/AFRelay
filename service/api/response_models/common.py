
from pydantic import BaseModel, ConfigDict, Field


class Obs(BaseModel):
    Code: int
    Msg: str | None = None

class Observaciones(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    obs: list[Obs] | None = Field(None, alias="Obs")

class Evt(BaseModel):
    Code: int
    Msg: str

class Events(BaseModel):
    Evt: list[Evt]

class Err(BaseModel):
    Code: int
    Msg: str

class Errors(BaseModel):
    Err: list[Err]

class FECAEASinMov(BaseModel):
    CAEA: str
    FchProceso: str
    PtoVta: int

######### Infrastructure #########
class ErrorDetails(BaseModel):
    method: str
    error_type: str
    details: str

class APIErrorResponseModel(BaseModel):
    status: str
    error: ErrorDetails
