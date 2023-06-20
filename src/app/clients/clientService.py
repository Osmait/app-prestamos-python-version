from src.domain.client.Client import Client
from src.domain.client.client_repository import ClientRepository
from src.infraestructure.models.client import ClientDto
import uuid


class ClientService:
    def __init__(self,clientRepository:ClientRepository) -> None:
       self.clientRepository = clientRepository
        
    def findAll(self)-> list[Client]:
        return self.clientRepository.find_all()
    
    def create(self,client:ClientDto)-> None:
        new_client = Client(**client.dict())
        # new_client.id = uuid.uuid4()
        self.clientRepository.create(new_client)
    


