from fastapi import FastAPI

from service.api.models.invoice import RootModel
from service.controllers.readiness_health_controller import \
    readiness_health_check
from service.controllers.request_invoice_controller import \
    request_invoice_controller
from service.utils.convert_to_dict import convert_pydantic_model_to_dict
from service.utils.logger import logger

app = FastAPI()

@app.post("/wsfe/invoice")
def generate_invoice(sale_data: RootModel) -> dict:
    
    logger.info("Invoice generation request received. Parsing input data and calling controller.")

    sale_data = convert_pydantic_model_to_dict(sale_data)
    invoice_result = request_invoice_controller(sale_data)

    return invoice_result

# ===================
# == HEALTH CHECKS ==
# ===================

@app.get("/health/liveness")
def liveness() -> dict:

    return {"health" : "OK"}

@app.get("/health/readiness")
def readiness() -> dict:

    status = readiness_health_check()
    return status
