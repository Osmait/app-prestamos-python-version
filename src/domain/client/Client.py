from src.infraestructure.config.database import Base
from sqlalchemy import Column,DateTime,String
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime



class Client(Base):
    __tablename__="clients"
    id = Column(String, primary_key=True, default=uuid.uuid4)
    name = Column(String,nullable=False)
    last_name =Column(String,nullable=False)
    phone =Column(String,nullable=False)
    address =Column(String,nullable=False)
    email= Column(String,nullable=False)
    deleted =Column(String,nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # loans = relationship("loans", back_populates="clients")

  