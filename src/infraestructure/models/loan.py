from pydantic import Field,BaseModel,ValidationError,validator,PydanticValueError
from datetime import datetime
from src.infraestructure.models.Frecuency import Frecuency
from src.infraestructure.controller.exceptions.custon_exceptions import NotFoundException

# class BadRequest(PydanticValueError):
#     code = "404"
#     msg_template = 'value is not "{wrong_value}"'


class LoanDto(BaseModel):
    amount:float = Field(gt=1)
    payment_date:datetime = Field(alias="paymentDate")
    second_paymentDate:datetime = Field(alias="secondPaymenDate")
    interest:float =Field()
    amount_of_payments:int =Field(alias="amountOfPayments")
    frequency:Frecuency =Field()
    client_id:str = Field(min_length=1, max_length=50, alias="clientId")

 


   