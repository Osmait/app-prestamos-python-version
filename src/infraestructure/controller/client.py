from fastapi import APIRouter
from src.app.clients.clientService import ClientService


client_routes = APIRouter()
client_servises = ClientService()


@client_routes.get("/client")
def get_clients():
    return  client_servises.findAll()