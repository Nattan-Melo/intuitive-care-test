import pandas as pd
import re
from fastapi import FastAPI,Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing_extensions import Annotated 

from models.reference import *
from models.response_dto import *
from models.request_dto import RequestDto
from services.repository import Repository

_DB_SOURCE_PATH = "Relatorio_cadop.csv"
_DATA_SOURCE_PATH = _DB_SOURCE_PATH

def getDataSource() -> pd.DataFrame:
    return pd.read_csv(_DATA_SOURCE_PATH, sep=";")

app = FastAPI()
database:DataFrame = getDataSource()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/api/resources")
async def getDataByAnsCode(req: RequestDto, repository: Annotated[Repository, Depends(Repository)]):
    ref: Reference = None
    dataSet: DataFrame = DataFrame()
    
    # ANSreq.
    if req.typeSearch == 0:
        if re.match("^\d+$",req.value) == None or re.match("\W",req.value) != None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
        ref = ANS()
        dataSet = repository.getDataBy(database, ref, req.value)
    # CNPJ
    elif req.typeSearch == 1:
        if re.match("^\d+$",req.value) == None and re.match("\W",req.value) != None or len(req.value) > 14 or len(req.value) < 14 :
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
        ref = CNPJ()
        dataSet = repository.getDataBy(database, ref, req.value)
    # MODALIDADE
    elif req.typeSearch == 2:
        if re.match("^\d+$",req.value) != None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
        ref = Modalidade()
        dataSet = repository.getDataBy(database, ref, req.value)

        listDto: list[ResponseDto] = []

        for index, row in dataSet.iterrows():
            listDto.append(ResponseDto(ANS=row['Registro_ANS'],
                                   CNPJ=row['CNPJ'],
                                   RazaoSocial=row['Razao_Social'],
                                   Email=row['Endereco_eletronico'],
                                   DataRegistro=row['Data_Registro_ANS'],
                                   Modalidade=row['Modalidade']))
            
        return listDto
        
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
    dto: ResponseDto = ResponseDto(ANS=dataSet['Registro_ANS'].values[0].item(),
                                   CNPJ=dataSet['CNPJ'].values[0].item(),
                                   RazaoSocial=dataSet['Razao_Social'].values[0],
                                   Email=dataSet['Endereco_eletronico'].values[0],
                                   DataRegistro=dataSet['Data_Registro_ANS'].values[0],
                                   Modalidade=dataSet['Modalidade'].values[0])
    return dto
    
