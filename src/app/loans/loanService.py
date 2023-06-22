from src.domain.loan.Loan import Loan
from src.domain.loan.loan_repository import LoanRepository
from src.infraestructure.models.loan import LoanDto
from datetime import datetime
from src.infraestructure.models.Frecuency import Frecuency




class LoanService:
    def __init__(self,loanRepository:LoanRepository) -> None:
       self.loanRepository = loanRepository
        
    def findAll(self,id:str)-> list[Loan]:
        return self.loanRepository.find_by_client_id(id);
    
    def create(self,loan:LoanDto)-> None:
        new_client = Loan(**loan.dict())
        self.loanRepository.create(new_client)
    
    def findAllByDAte(self) -> list[Loan]:
        listofLoan = self.loanRepository.find_all()
        loanlistReponse = []
        for loan in listofLoan:
            if is_payment_due(loan,datetime.now()):
                loanlistReponse.append(loan)
        
        return loanlistReponse
    


def is_payment_due(payment:Loan,currentDate:datetime):
    if payment.frequency  == Frecuency.BIWEEKLY:
        return payment.payment_date.day == currentDate.day or payment.second_paymentDate.day == currentDate.day





    