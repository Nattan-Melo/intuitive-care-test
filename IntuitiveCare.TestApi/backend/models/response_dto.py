from pydantic import BaseModel

class ResponseDto(BaseModel):
    ANS:  int = 0
    CNPJ: int  = 0
    RazaoSocial: str = ' '
    DataRegistro: str = ' '
    Email: str = ' '
    Modalidade: str = ' '
    