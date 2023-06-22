from fastapi import FastAPI
from src.infraestructure.controller.health_cheack import health_check_router
from src.infraestructure.controller.client import client_routes
from src.infraestructure.controller.loan import loan_routes
from src.infraestructure.controller.transaction import transaction_routes
from src.infraestructure.config.database import Base,engine

from src.infraestructure.controller.exceptions.error_handler import not_found_exception_handler
from src.infraestructure.controller.exceptions.custon_exceptions import NotFoundException



app = FastAPI()


# Hander Errors
app.add_exception_handler(NotFoundException,not_found_exception_handler)


# Migration Init
# Base.metadata.drop_all(engine)
# Base.prepare(autoload_with=engine)
Base.metadata.create_all(bind=engine)



# Routes
app.include_router(health_check_router)
app.include_router(client_routes)
app.include_router(loan_routes)
app.include_router(transaction_routes)






