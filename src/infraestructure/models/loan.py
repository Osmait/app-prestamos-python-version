from pydantic import Field,BaseModel
from datetime import datetime


class LoanDto(BaseModel):

    payment_date:datetime = Field(alias="paymentDate")
    second_paymentDate:datetime = Field(alias="secondPaymenDate")
    interest:float =Field()
    amount_of_payments:int =Field(alias="amountOfPayments")
    frequency:str = Field(min_length=1, max_length=50)
    client_id:str = Field(min_length=1, max_length=50, alias="clientId")
   