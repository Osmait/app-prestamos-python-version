from src.domain.loan.Loan import Loan
from src.domain.loan.loan_repository import LoanRepository
from src.infraestructure.models.loan import LoanDto
import uuid
from datetime import datetime

class LoanService:
    def __init__(self,loanRepository:LoanRepository) -> None:
       self.loanRepository = loanRepository
        
    def findAll(self)-> list[Loan]:
        return self.loanRepository.find_all()
    
    def create(self,loan:LoanDto)-> None:
        # newdate =  datetime.strptime(loan.payment_date,'%Y-%m-%d').date()
        # newdate2 =  datetime.strptime(loan.payment_date,'%Y-%m-%d').date()

        # loan.payment_date = newdate
        # loan.second_paymentDate = newdate2
        new_client = Loan(**loan.dict())
        self.loanRepository.create(new_client)
    