# Intuitive Care Test

## Estrutura do projeto
- IntuitiveCare.WebScraping
    projeto feito em python que realiza web scraping para baixar dois anexos em PDF e salvar em formato .zip
- IntuitiveCare.DataTransformation:
    Projeto para transformar dados realizando uma verificação estrutural no arquivo .csv e realizando substituições
    de texto em colunas 
- IntuitiveCare.SQL:
    Arquivo de consulta em SQL
- IntuitiveCare.TestApi:
    Dividido em Backend (API desenvolvida em FastApi) e Frontend (projeto desenvolvido em Vuejs para consulta de dados)

## Demostrativo Postman

### Busca com código ANS
![alt text](https://github.com/Nattan-Melo/intuitive-care-test/blob/master/img/ans.png "Teste com código ANS")

### Busca por CNPJ
![alt text](https://github.com/Nattan-Melo/intuitive-care-test/blob/master/img/cnpj.png "Teste com CNPJ")

### Busca textual por Modalidade
![alt text](https://github.com/Nattan-Melo/intuitive-care-test/blob/master/img/modalidade.png)

## Bibliotecas e recursos utilizados nesse projeto

- tabula-py: https://github.com/chezou/tabula-py;
- pandas: https://github.com/pandas-dev/pandas;
- fastapi: https://github.com/fastapi/fastapi;


