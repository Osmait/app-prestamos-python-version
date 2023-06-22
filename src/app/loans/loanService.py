from src.domain.loan.Loan import Loan
from src.domain.loan.loan_repository import LoanRepository
from src.infraestructure.models.loan import LoanDto
from datetime import datetime
from src.infraestructure.models.Frecuency import Frecuency




class LoanService:
    def __init__(self,loanRepository:LoanRepository) -> None:
       self.loanRepository = loanRepository
       
        
    def find_all(self,id:str)-> list[Loan]:
        return self.loanRepository.find_by_client_id(id);

    
    def create(self,loan:LoanDto)-> None:
        new_client = Loan(**loan.dict())
        self.loanRepository.create(new_client)

    
    def find_all_by_Date(self,id:str) -> list[Loan]:
        current_date = datetime.now()
        listofLoan = self.loanRepository.find_by_client_id(id)
        return [ loan for loan in listofLoan if self._is_payment_due(loan,current_date)]
    
    
    def _is_payment_due(self,payment:Loan,current_date:datetime) -> bool:
        if payment.frequency  == Frecuency.BIWEEKLY:
            return (payment.payment_date.day == current_date.day 
                    or payment.second_paymentDate.day == current_date.day)

    







    