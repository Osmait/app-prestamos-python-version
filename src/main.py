from fastapi import FastAPI
from src.infraestructure.controller.health_cheack import health_check_router
from src.infraestructure.controller.client import client_routes
from src.infraestructure.controller.loan import loan_routes
from src.infraestructure.controller.transaction import transaction_routes
from src.infraestructure.config.database import Base,engine



app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(health_check_router)
app.include_router(client_routes)
app.include_router(loan_routes)
app.include_router(transaction_routes)





