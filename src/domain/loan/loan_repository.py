
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