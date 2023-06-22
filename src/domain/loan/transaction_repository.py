from src.infraestructure.config.database import Session
from src.domain.loan.Loan import Transaction


class TransactionRepository:
    def __init__(self) -> None:
        self.db = Session()
    
    def find_all(self):
        return self.db.query(Transaction).all()
    
    def create(self,transaction:Transaction):
        self.db.add(transaction)
        self.db.commit()
    