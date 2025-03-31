from pandas import DataFrame
from models.reference import Reference

class Repository:
    def getDataBy(self, db: DataFrame, ref: Reference, value_ref: str)  -> DataFrame:
        return ref.dataSearch(db, value_ref)