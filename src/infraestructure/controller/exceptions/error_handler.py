from fastapi import Request
from fastapi.responses import JSONResponse
from src.infraestructure.controller.exceptions.custon_exceptions import NotFoundException




async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404, 
        content={"message": "not found","status": 404},
    )

