
import os
import pandas as pd

from utils.normalize import normalizar_texto


def exportar_csv(df,workspace_name,sheet_id,sheet_name,pasta_raiz="data"):

    # Normaliza os nomes
    workspace_folder = normalizar_texto(workspace_name)
    sheet_folder = normalizar_texto(sheet_name)

    # Cria caminho do workspace
    folder_workspace = os.path.join(pasta_raiz,workspace_folder)

    os.makedirs(folder_workspace, exist_ok=True)

    # Cria caminho da planilha
    nome_pasta_planilha = f"{sheet_id}_{sheet_folder}"

    folder_planilha = os.path.join(folder_workspace,nome_pasta_planilha)

    # Caminho do CSV
    caminho_csv = folder_planilha+".csv"
    
    # Exporta DataFrame
    df.to_csv(caminho_csv,encoding="utf-8-sig",index=False)

    print(f"Arquivo exportado: {caminho_csv}")

    return caminho_csv