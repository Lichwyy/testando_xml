import xml.etree.ElementTree as ET
from class_auto_d import caminho_arquivo

class XMLToDict():
    def __init__(self):
        self.dicionario = dict()
        self.tree = ET.parse(caminho_arquivo)
        self.root = self.tree.getroot()

    def xml_to_dict(self, despacho):
        dicionario_despacho = dict()
        for tag in despacho:
            if list(tag):
                dicionario_despacho[tag.tag] = self.xml_to_dict(tag)
            else:
                dicionario_despacho[tag.tag] = tag.text.strip() if tag.text else None
        return dicionario_despacho
    
    def percorrendo_xml(self):
        for i, despacho in enumerate(self.root.findall("./despacho")):
            self.dicionario[f'despacho_{i+1}'] = self.xml_to_dict(despacho)

xmltodict = XMLToDict()

xmltodict.percorrendo_xml()
print(xmltodict.dicionario)