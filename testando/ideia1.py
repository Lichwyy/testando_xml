import xml.etree.ElementTree as ET

def despacho_para_dict(despacho):
    """Transforma um elemento <despacho> em um dicionário dinâmico."""
    despacho_dict = {}

    for tag in despacho:
        if list(tag):  # Se a tag tem filhos, trata como sub-dicionário
            despacho_dict[tag.tag] = despacho_para_dict(tag)
        else:
            despacho_dict[tag.tag] = tag.text.strip() if tag.text else None

    return despacho_dict

# Carrega o XML
tree = ET.parse("Patente_2828_18032025.xml")
root = tree.getroot()

# Dicionário para armazenar todos os despachos
despachos_dict = {}

# Percorre todos os elementos <despacho>
for i, despacho in enumerate(root.findall("./despacho")):
    despachos_dict[f"despacho_{i+1}"] = despacho_para_dict(despacho)

# Exibindo o resultado
import json
# print(json.dumps(despachos_dict, indent=4, ensure_ascii=False))


print(despachos_dict['despacho_1000'])