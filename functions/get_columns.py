import requests

def get_columns(url, headers, sheet_id):

    response = requests.get(url.format(sheet_id),headers=headers,timeout=30)

    response.raise_for_status()

    resultado = response.json()

    colunas = {
        coluna["columnId"]: coluna["title"]
        for coluna in resultado.get("items", [])
    }

    return colunas