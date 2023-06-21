from fastapi import APIRouter
from src.infraestructure.controller.exceptions.error_handler import NotFoundException


transaction_routes = APIRouter(prefix="/api/v1")


@transaction_routes.get("/transaction")
def get_transaction():
    raise NotFoundException("holaa")