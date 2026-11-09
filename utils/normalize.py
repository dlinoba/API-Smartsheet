
import re
import unicodedata


def normalizar_texto(texto):

    texto = unicodedata.normalize('NFKD', str(texto))
    texto = texto.encode('ASCII', 'ignore').decode('ASCII')

    # Remove caracteres especiais
    texto = re.sub(r'[^\w\s-]', '', texto)

    # Substitui espaços por _
    texto = re.sub(r'\s+', '_', texto.strip())

    return texto
