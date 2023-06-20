from fastapi.testclient import TestClient
from fastapi import status
from src.main import app
# from testcontainers.postgres import PostgresContainer
# import sqlalchemy

# with PostgresContainer("postgres:9.5") as postgres:
#     engine = sqlalchemy.create_engine(postgres.get_connection_url())
   

client = TestClient(app)

def test_get_clients():
   response = client.get("/api/v1/client")
   assert response.status_code == status.HTTP_200_OK

