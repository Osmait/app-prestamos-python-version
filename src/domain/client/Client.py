from src.infraestructure.config.database import Base
from sqlalchemy import Column,Integer,String
import uuid



class Client(Base):
    __tablename__="clients"

    id  = Column(String,primary_key= True, default= uuid.uuid4)
    name = Column(String,nullable=False)
    last_name =Column(String,nullable=False)
    phone =Column(String,nullable=False)
    address =Column(String,nullable=False)
    email= Column(String,nullable=False)
    deleted =Column(String,nullable=False)
  