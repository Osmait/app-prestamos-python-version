from fastapi import APIRouter,status
from fastapi.responses import JSONResponse
from src.app.clients.clientService import ClientService
from src.domain.client.client_repository import ClientRepository
from src.infraestructure.models.client import ClientDto


client_routes = APIRouter( prefix="/api/v1")
client_repository = ClientRepository()
client_servises = ClientService(client_repository)



@client_routes.get("/client")
def get_clients():
    return  client_servises.findAll()

@client_routes.post("/client",response_model=dict)
def create_client(client:ClientDto):
    client_servises.create(client)
    return JSONResponse(status_code=status.HTTP_201_CREATED , content="Created")
   