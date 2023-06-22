
from src.infraestructure.config.database import Session
from src.domain.loan.Loan import Loan



class LoanRepository:
    
    def __init__(self) -> None:
        self.db = Session()
    
    def find_all(self):
        return self.db.query(Loan).all()
    
    def create(self,loan:Loan):
        self.db.add(loan)
        self.db.commit()
    
    def find_by_client_id(self,id:str):
      return  self.db.query(Loan).filter(Loan.client_id == id).all()
