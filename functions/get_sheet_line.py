import requests

def get_sheet_line(url, headers, sheet_id, colunas, limit=250):

    offset = 0
    registros = []

    while True:

        params = {"offset": offset,"limit": limit}

        response = requests.get(url.format(sheet_id),headers=headers,params=params,timeout=30)

        response.raise_for_status()

        resultado = response.json()

        linhas = resultado.get("items", [])

        for linha in linhas:

            registro = {
                "sheetId": sheet_id,
                "rowId": linha.get("rowId"),
                "rowNumber": linha.get("rowNumber"),
                "createdAt": linha.get("createdAt"),
                "modifiedAt": linha.get("modifiedAt")
            }

            for celula in linha.get("cells", []):

                nome_coluna = colunas.get(celula.get("columnId"))

                if nome_coluna:
                    registro[nome_coluna] = celula.get("value")

            registros.append(registro)

        if not linhas:
            break

        offset += len(linhas)

        if offset >= resultado.get("total", 0):
            break

    return registros