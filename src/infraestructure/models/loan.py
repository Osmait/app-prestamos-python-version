from pydantic import Field,BaseModel
from datetime import datetime
from src.infraestructure.models.Frecuency import Frecuency


class LoanDto(BaseModel):

    payment_date:datetime = Field(alias="paymentDate")
    second_paymentDate:datetime = Field(alias="secondPaymenDate")
    interest:float =Field()
    amount_of_payments:int =Field(alias="amountOfPayments")
    frequency:Frecuency =Field()
    client_id:str = Field(min_length=1, max_length=50, alias="clientId")


    # @property
    # def frequency_enum(self) -> Frecuenty:
    #     return Frecuenty(self.frequency)

   