from pydantic import Field,BaseModel


class ClientDto(BaseModel):
    name:str = Field(min_length=1, max_length=50)
    last_name:str =Field(min_length=1, max_length=50,alias="lastName")
    phone:str =Field(min_length=1, max_length=50)
    address:str =Field(min_length=1, max_length=50)
    email:str= Field(min_length=1, max_length=50)