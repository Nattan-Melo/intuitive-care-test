import tabula
import os
import pandas as pd
from zipfile import ZipFile
import pathlib

_CVS_FILE = "Anexo_1.csv"
_PDF_FILE = "Anexo_1.pdf"
_OUTPUT_FILE = "novo_anexo"

file_csv = pathlib.Path(_CVS_FILE)
tabula.convert_into(_PDF_FILE, _CVS_FILE, output_format='csv', pages='3-181')
dt_anexo = pd.read_csv(_CVS_FILE, sep=',')

dt_anexo.drop(dt_anexo.index[(dt_anexo["VIGÊNCIA"]=="VIGÊNCIA")], axis=0, inplace=True)

dt_anexo = dt_anexo.rename(columns={
     'OD':'Seg. Odontológica', 'AMB':'Seg. Ambulatorial'
})

dt_anexo.to_csv(f"{_OUTPUT_FILE}.csv")

with ZipFile(f"{_OUTPUT_FILE}.zip", 'w') as zp:
     zp.write(f"{_OUTPUT_FILE}.csv")
     
os.remove(f"{_OUTPUT_FILE}.csv")
os.remove(_CVS_FILE)




# if file_resource.is_file() == False:
#     tabula.convert_into(f"{_RES_PATH}/{_WORK_PDF_FILE}", _RES_PATH+"/anexo_1.csv", output_format='csv', pages='all')

# else:
#     dt_csv = pd.read_csv(_RES_PATH+"/anexo_1.csv", on_bad_lines='skip')
#     print(dt_csv)
    
