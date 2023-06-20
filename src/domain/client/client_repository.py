from src.infraestructure.config.database import Session
from src.domain.client.Client import Client

class ClientRepository:
    def __init__(self) -> None:
        self.db = Session()
    
    def find_all(self):
        return self.db.query(Client).all()
    
    def create(self,client:Client):
        self.db.add(client)
        self.db.commit()
       