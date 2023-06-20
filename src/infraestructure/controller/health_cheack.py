from fastapi import APIRouter



health_check_router = APIRouter()

@health_check_router.get("/health-check")
def health_check():
    return "Server Up"