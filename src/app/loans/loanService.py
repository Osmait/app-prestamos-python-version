from src.domain.loan.Loan import Loan
from src.domain.loan.loan_repository import LoanRepository
from src.infraestructure.models.loan import LoanDto
from datetime import datetime
from src.infraestructure.models.Frecuency import Frecuency


def is_payment_due(payment:Loan,currentDate:datetime):
    if payment.frequency  == Frecuency.BIWEEKLY:
        return payment.payment_date.day == currentDate.day or payment.second_paymentDate.day == currentDate.day



class LoanService:
    def __init__(self,loanRepository:LoanRepository) -> None:
       self.loanRepository = loanRepository
        
    def findAll(self)-> list[Loan]:
        return self.loanRepository.find_all()
    
    def create(self,loan:LoanDto)-> None:
        new_client = Loan(**loan.dict())
        self.loanRepository.create(new_client)
    
    def findAllByDAte(self):
        listofLoan = self.loanRepository.find_all()
        loanlistReponse = []
        for loan in listofLoan:
            if is_payment_due(loan,datetime.now()):
                loanlistReponse.append(loan)
        
        return loanlistReponse



    