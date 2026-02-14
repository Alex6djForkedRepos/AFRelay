from pydantic import BaseModel

from service.api.request_models.common import Auth


class FeCompConsReq(BaseModel):
    PtoVta: int
    CbteTipo: int
    CbteNro: int

class FECompConsultar(BaseModel):
    Auth: Auth
    FeCompConsReq: FeCompConsReq
