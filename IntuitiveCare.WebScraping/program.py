from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from zipfile import ZipFile
from bs4 import BeautifulSoup
import re
import os




_ANSS_PAGE = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

try:
    html = urlopen(_ANSS_PAGE)
    bs = BeautifulSoup(html.read(), 'html.parser')
    anexosCount: int = 0
    for anexo in bs.find_all('a', string=re.compile('Anexo I',re.I)):
        if anexo.attrs['href'].endswith('.pdf') == True:
            anexosCount = anexosCount + 1
            req = Request(anexo.attrs['href'])
            res = urlopen(req)
            pdf = open("Anexo_"+str(anexosCount)+".pdf", 'wb')
            pdf.write(res.read())
            pdf.close()
              
except HTTPError as e:
    print(e)

except URLError as e:
    print("O servidor não foi encontrado")

work_dir = os.getcwd()
files_report = os.listdir(work_dir)
pdf_files = [file for file in files_report if file.endswith('.pdf')]

zip_name = 'anexos.zip'
with ZipFile(zip_name, 'w') as zp:
    for file in pdf_files:
        zp.write(file, file)
        os.remove(file)





