from fastapi import APIRouter


loan_routes = APIRouter()

@loan_routes.get("/loan")
def get_loans():
    return "loans list"
