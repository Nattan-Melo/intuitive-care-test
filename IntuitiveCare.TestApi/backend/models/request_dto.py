from pydantic import BaseModel

class RequestDto(BaseModel):
    value: str = ' '
    typeSearch: int = 0
    