import requests

def get_sheet(url, headers, workspace_id, limit=250):

    offset = 0
    registros = []

    while True:

        params = {"offset": offset,"limit": limit}

        response = requests.get(url.format(workspace_id),headers=headers,params=params,timeout=30)

        response.raise_for_status()

        resultado = response.json()

        planilhas = resultado.get("items", [])

        for planilha in planilhas:

            registros.append({
                "workspaceId": workspace_id,
                "sheetId": planilha.get("sheetId"),
                "name": planilha.get("name"),
                "createdAt": planilha.get("createdAt"),
                "modifiedAt": planilha.get("modifiedAt")
            })

        if len(planilhas) < limit:
            break

        offset += len(planilhas)

    return registros