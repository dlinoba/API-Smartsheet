import os
import pandas as pd
from dotenv import load_dotenv

from functions.get_workspace import get_workspace
from functions.get_sheet import get_sheet
from functions.get_columns import get_columns
from functions.get_sheet_line import get_sheet_line
from utils.export import exportar_csv

load_dotenv()

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
}

root_url = os.getenv("root_url")

url_workspaces = root_url + "workspaces"
url_planilhas = root_url + "planilhas?workspaceId={}"
url_colunas = root_url + "planilhas/{}/colunas"
url_linhas = root_url + "planilhas/{}/linhas"

# ==========================================
# WORKSPACES
# ==========================================

workspaces = get_workspace(url_workspaces,headers)

# ==========================================
# PLANILHAS
# ==========================================

for workspace in workspaces:

    workspace_id = workspace["workspaceId"]

    planilhas = get_sheet(url_planilhas,headers,workspace_id)

    for planilha in planilhas:

        sheet_id = planilha["sheetId"]

        # Busca colunas
        colunas = get_columns(url_colunas,headers,sheet_id)

        # Busca linhas
        linhas = get_sheet_line(url_linhas,headers,sheet_id,colunas)

        # DataFrame
        df = pd.DataFrame(linhas)
        #drop colunas apenas de controle.
        df.drop(columns=["sheetId","rowId","rowNumber","createdAt","modifiedAt"],inplace=True,errors="ignore")
        #dropa linhas onde todas as colunas são NaN
        df = df.dropna(how="all")
        

        export = exportar_csv(df=df,workspace_name=workspace["name"],sheet_id=sheet_id,sheet_name=planilha["name"],pasta_raiz="data")

        # Exportação
        print(f"Planilha processada: {planilha['name']}")
        print(f"Planilha exportada: {export}")