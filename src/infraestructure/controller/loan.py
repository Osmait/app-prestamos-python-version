from fastapi import APIRouter,status
from fastapi.responses import JSONResponse
from src.app.loans.loanService import LoanService
from src.domain.loan.loan_repository import LoanRepository
from src.infraestructure.models.loan import LoanDto

loan_repository = LoanRepository()
loan_service = LoanService(loan_repository)

loan_routes = APIRouter(prefix="/api/v1")

@loan_routes.get("/loan")
def get_loans():
    return  loan_service.findAll()

@loan_routes.post("/loan")
def post_loans(loan:LoanDto):
    loan_service.create(loan)
    return JSONResponse(status_code=status.HTTP_201_CREATED , content="Created")
