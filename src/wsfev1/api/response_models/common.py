from typing import Dict

from pydantic import BaseModel


class Obs(BaseModel):
    Code: int
    Msg: str | None = None

class Observaciones(BaseModel):
    obs: list[Obs] | Dict

class Evt(BaseModel):
    Code: int
    Msg: str

class Events(BaseModel):
    Evt: list[Evt] | Dict

class Err(BaseModel):
    Code: int
    Msg: str

class Errors(BaseModel):
    Err: list[Err] | Dict