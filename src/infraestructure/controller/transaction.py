from fastapi import APIRouter


transaction_routes = APIRouter()

@transaction_routes.get("/transaction")
def get_transaction():
    return "transaction list"