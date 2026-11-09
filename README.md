#API-Smartsheet

Integração em Python para coleta, organização e exportação de dados da API Smartsheet.

Sobre o projeto

Este projeto tem como objetivo automatizar a extração de dados do Smartsheet, permitindo consultar workspaces, planilhas, colunas e linhas, organizando as informações em arquivos CSV.

A aplicação utiliza Python para realizar as requisições HTTP, processar os dados retornados pela API e estruturar os arquivos exportados em diretórios organizados por workspace e planilha.

Funcionalidades
Workspaces: consulta todos os workspaces disponíveis, utilizando paginação.
Planilhas: identifica as planilhas vinculadas a cada workspace.
Colunas: consulta as colunas de cada planilha e seus respectivos identificadores.
Linhas: extrai os registros das planilhas, associando os valores aos nomes das colunas.
Paginação: permite recuperar grandes volumes de registros por meio de requisições paginadas.
Normalização: remove acentos e caracteres especiais dos nomes utilizados nos diretórios.
Exportação: converte os dados extraídos em DataFrames e exporta arquivos CSV.
Tecnologias utilizadas
Python
Requests
Pandas
Python Dotenv
Estrutura do projeto
text
API-Smartsheet/
│
├── functions/
│   ├── get_workspace.py
│   ├── get_sheet.py
│   ├── get_columns.py
│   └── get_sheet_line.py
│
├── utils/
│   ├── normalize.py
│   └── export.py
│
├── data/
│   └── (arquivos exportados)
│
├── .env
├── .env_example
├── requirements.txt
├── main.py
└── README.md

Organização dos módulos
Módulo	Descrição
get_workspace.py	Consulta e retorna os workspaces.
get_sheet.py	Consulta as planilhas de um workspace.
get_columns.py	Consulta as colunas de uma planilha.
get_sheet_line.py	Consulta as linhas e associa os valores aos nomes das colunas.
normalize.py	Normaliza textos e nomes de diretórios.
export.py	Organiza diretórios e exporta os DataFrames em CSV.
main.py	Controla e executa o processo de extração.
Instalação
1. Clonar o repositório
bash
git clone https://github.com/dlinoba/API-Smartsheet.git

2. Acessar o diretório
bash
cd API-Smartsheet

3. Instalar as dependências
bash
pip install -r requirements.txt

4. Configurar as variáveis de ambiente

Crie um arquivo .env na raiz do projeto, utilizando o .env_example como referência.

Configure as seguintes variáveis:

env
API_TOKEN=SEU_TOKEN_SMARTSHEET
root_url=URL_BASE_DA_API


Importante: não compartilhe seu token de acesso e não envie o arquivo .env para o GitHub.

Execução

Para iniciar o processo de extração, execute:

bash
python main.py


O processo seguirá as seguintes etapas:

Consulta todos os workspaces disponíveis.
Identifica as planilhas vinculadas a cada workspace.
Consulta as colunas de cada planilha.
Recupera todas as linhas utilizando paginação.
Organiza os dados em DataFrames.
Exporta os dados em arquivos CSV.
Estrutura dos dados exportados

Os arquivos são organizados por workspace e planilha.

Exemplo:

text
data/
│
├── Reforma_Tributaria_2026/
│   │
│   ├── 12345_Controle_Geral/
│   │   └── Controle_Geral.csv
│   │
│   └── 12346_Cronograma/
│       └── Cronograma.csv
│
└── Integracao_JIRA/
    │
    └── 78901_Projetos_JIRA/
        └── Projetos_JIRA.csv


Os diretórios são criados automaticamente durante a execução, caso ainda não existam.

Tratamento dos dados

Durante a extração, os dados são organizados utilizando Pandas.

As informações de identificação e controle das linhas podem ser removidas do DataFrame exportado, mantendo os dados de negócio das planilhas.

Os arquivos CSV são exportados utilizando codificação UTF-8 com BOM (utf-8-sig), facilitando sua abertura no Microsoft Excel.

Segurança
As credenciais são armazenadas em variáveis de ambiente.
O token de acesso não deve ser versionado.
O arquivo .env deve permanecer fora do controle de versão.
O arquivo .env_example deve conter apenas valores ilustrativos.
Autor

dlinoba

GitHub: @dlinoba

Projeto desenvolvido em Python para automatização da coleta e organização de dados do Smartsheet.
