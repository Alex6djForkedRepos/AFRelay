from pydantic import BaseModel, Field


class ErrorDetails(BaseModel):
    method: str
    error_type: str
    details: str

class APIErrorResponseModel(BaseModel):
    status: str
    error: ErrorDetails | None = Field(None, alias="error")