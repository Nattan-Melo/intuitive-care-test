from abc import ABC, abstractmethod
from models import DataFrame

class Reference(ABC):
    @abstractmethod
    def dataSearch(self, db: DataFrame, value_ref: str):
        pass
    
class ANS(Reference):
    def dataSearch(self, db: DataFrame, value_ref:str)  -> DataFrame:
        return db.loc[db['Registro_ANS']==int(value_ref)]
    
class CNPJ(Reference):
    def dataSearch(self, db: DataFrame, value_ref:str)  -> DataFrame:
        return db.loc[db['CNPJ']==int(value_ref)]
    

class Modalidade(Reference):
    def dataSearch(self, db: DataFrame, value_ref:str)  -> DataFrame:
        return db.loc[db['Modalidade']==value_ref]

