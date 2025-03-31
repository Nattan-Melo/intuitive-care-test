
import logging
import pytest
logger = logging.getLogger(__name__)
from models.reference import *
from services.repository import *
from app import getDataSource

class TestContext():
    
    def test_get_report_data_by_ANS(self):
        ref: Reference = Modalidade()
        repo: Repository = Repository()
        dataSet = repo.getDataBy(getDataSource(),ref, 'Administradora de Benefícios')
        for index, row in dataSet.iterrows():
            logger.info(f"-> index {index} - row {row['CNPJ']}")
            
        return True
    
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_database_source(self):
        db = getDataSource()
        logger.info(db.loc[db['Registro_ANS']==419761, 'CNPJ'])
        assert True