from src.infraestructure.config.database import Base
from sqlalchemy import Column,DateTime,String,Float,Integer,Boolean,ForeignKey
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime





class Loan(Base):
    __tablename__="loans"
    id = Column(String, primary_key=True, default=uuid.uuid4)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime,nullable=False)
    second_paymentDate = Column(DateTime,nullable=False)
    interest =Column(Float,nullable=False)
    amount_of_payments =Column(Integer,nullable=False)
    is_Paid = Column(Boolean,nullable=False, default=False)
    frequency = Column(String,nullable=False)
    deleted =Column(Boolean,nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    client_id = Column(String,ForeignKey("clients.id"))
    client = relationship("Client", back_populates="loans")



  