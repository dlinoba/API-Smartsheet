import requests

def get_workspace(url, headers, limit=250):

    offset = 0
    registros = []

    while True:

        params = {"offset": offset,"limit": limit}

        response = requests.get(url,headers=headers,params=params,timeout=30)

        response.raise_for_status()

        resultado = response.json()

        linhas = resultado.get("items", [])

        for linha in linhas:

            registros.append({
                "workspaceId": linha.get("workspaceId"),
                "name": linha.get("name")
            })

        if len(linhas) < limit:
            break

        offset += limit

    return registros