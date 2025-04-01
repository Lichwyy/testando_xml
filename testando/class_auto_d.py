from datetime import datetime
import requests
import os
import zipfile


class AutoDownload:
    def __init__(self):
        self.url_base = "https://revistas.inpi.gov.br/txt/P"
        self.contador = 2829
        self.data_atual = datetime(2025,3,25)
        self.pasta_extraidos = "Arquivos Extraídos"
        self.nome_xml = f"Arquivos Extraídos\\Patente{self.contador}.xml" # Arruma isso

    # def verificando_versao_atual(self):
    #     return os.path.exists(self.nome_xml)
    
    def encontrando_arquivo(self):
        # if self.verificando_versao_atual():
        #     return None
        url = f"{self.url_base}{self.versao_atual_RPI()}.zip"
        response = requests.head(url)
        if response.status_code == 200:
            return url, f"P{self.versao_atual_RPI()}"
        return 'não econtrado'
    
    def versao_atual_RPI(self):
        # if self.verificando_versao_atual():
        #     return None
        hoje = datetime.today()
        qtd_semanas = (hoje-self.data_atual).days // 7
        self.contador += qtd_semanas
        self.data_atual = hoje
        return self.contador
    
    def extraindo_arquivos(self):
        # if self.verificando_versao_atual():
        #     return None
        response = requests.get(self.encontrando_arquivo()[0], stream=True)
        if response.status_code == 200:
            with open(self.encontrando_arquivo()[1], "wb") as f:
                for chunck in response.iter_content(chunk_size=8192):
                    f.write(chunck)
    
    def colocando_arquivos_na_pasta(self):
        # if self.verificando_versao_atual:
        #     return None
        os.makedirs(self.pasta_extraidos, exist_ok=True)
        with zipfile.ZipFile(self.encontrando_arquivo()[1], "r") as zip_ref:
            zip_ref.extractall(self.pasta_extraidos)
        
        os.remove(self.encontrando_arquivo()[1])

    def renomeando_xml(self):
        # if self.verificando_versao_atual():
        #     return self.nome_xml
        caminho_base = f"Arquivos Extraídos\\Patente_{self.contador}_{self.data_atual.strftime("%d%m%Y")}.xml"
        os.rename(caminho_base, self.nome_xml)
        return self.nome_xml
    
autodownload = AutoDownload()
autodownload.extraindo_arquivos()
autodownload.colocando_arquivos_na_pasta()
caminho_arquivo = autodownload.renomeando_xml()


