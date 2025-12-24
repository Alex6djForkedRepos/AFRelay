from pydantic import BaseModel


class CompInfo(BaseModel):
    Cuit: int
    PtoVta: int
    CbteTipo: int