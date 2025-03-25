import xml.etree.ElementTree as ET

tree = ET.parse("Patente_2828_18032025.xml")
root = tree.getroot()

despachos = []

for despacho in root.findall("./despacho"):
    despacho_dict = {
        "codigo": despacho.findtext("codigo", default=None),
        "titulo": despacho.findtext("titulo", default=None),
        "comentario": despacho.findtext("comentario", default=None),
    }

    processo = despacho.find("processo-patente")
    if processo is not None:
        despacho_dict.update({
            "numero_processo": processo.findtext("numero", default=None),
            "data_deposito": processo.findtext("data-deposito", default=None),
        })

        # Extraindo titulares
        titulares = []
        titular_lista = processo.find("titular-lista")
        if titular_lista is not None:
            for titular in titular_lista.findall("titular"):
                titulares.append({
                    "nome": titular.findtext("nome-completo", default=None),
                    "uf": titular.findtext("endereco/uf", default=None),
                    "pais": titular.findtext("endereco/pais/sigla", default=None),
                })
        despacho_dict["titulares"] = titulares

    despachos.append(despacho_dict)

# Exibindo os dados extraídos
for d in despachos:
    print(d)

print(len(despachos))