import requests
import zipfile
import os
from datetime import datetime

def encontrando_arquivo(url_base: str, n_base: int):
        url = f"{url_base}{n_base}.zip"
        response = requests.head(url)

        if response.status_code == 200:
            return url, f"P{n_base}"
        return 'não econtrado'

def versao_atual_RPI():
    data_inicial = datetime(2025, 3, 25)
    contador = 2829
    hoje = datetime.today()

    qtd_semanas = (hoje-data_inicial).days // 7

    contador += qtd_semanas
    return contador

# P2829.zip
url_arquivo, nome_arquivo = encontrando_arquivo("https://revistas.inpi.gov.br/txt/P", versao_atual_RPI())
print(url_arquivo)

response = requests.get(url_arquivo, stream=True)
arquivos_extraidos = "Arquivos extraídos"
if response.status_code == 200:
    with open(nome_arquivo, "wb") as f:
        for chunck in response.iter_content(chunk_size=8192):
            f.write(chunck)

    print("Deu certo: ", nome_arquivo)

    os.makedirs(arquivos_extraidos, exist_ok=True)
    with zipfile.ZipFile(nome_arquivo, "r") as zip_ref:
        zip_ref.extractall(arquivos_extraidos)
    print("Arquivo extraído para: ", arquivos_extraidos)

    os.remove(nome_arquivo)
