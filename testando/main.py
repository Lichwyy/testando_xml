# Dados sobre os arquivos:

# Estruturação: <revista> trás atributos como <numero> número da edição RPI, <dataPublicacao> data da publicação dessa edição e <diretoria> área de relação do conteúdo (No caso, patente).
# <despacho> representará a decisão tomada em cima do pedido da patente, então seus atributos <codigo> identifica o tipo de decisão, <titulo> descrição do despache e <processo-patente> que 

# Identificadores INID (Internationally agreed Numbers for the Identification of Data) inidicam campos existentes na documentação de uma patente.
# INIDs:
# 11 - Número da patente
# 21 - Número do pedido da patente
# 22 - Data em que o pedido foi formalmente depositado
# 30 - Pedido de prioridade unionista, (Esse pedido diz respeito a caso um inventor queira patentear a sua invenção em outro país utilizando a data da patente original, ele possui 12 meses para fazer isso)
# 31 - Data em que o pedido prioritário foi depositado
# 32 - Número do pedido prioritário
# 33 - Sigla do país do pedido prioritário
# 43 - Data da publicação do pedido na revista oficial
# 45 - Data da concessão daquela patente
# 51 - Classificação técnica segundo o sistema internacional ICP
# 52 - Código de classificação específico do país
# 61 - Número do pedido principal que este pedido está vinculado (Pedido prioritário)
# 62 - Indica se o pedido atual é derivado de um pedido anterior
# 66 - É um pedido de prioridade interna, que um pedido nacional requisita prioridade sobre outro pedido nacional
# 71 - Nome do titular original do pedido
# 72 - Nome do(s) criadore(s)/inventore(s)
# 73 - Nome da pessoa, ou empresa que pertence a patente
# 85 - Data que indica quando um pedido internacional PCT entrou na fase internacional
# 86 - Número do pedido internacional no sistema PCT
# 87 - Data da públicação internacional da OMPI (Organização Mundial da Propriedade Intelectual)
# co - Comentário e observações sobre o despache e o seu código
# fg - Adiciona detalhes adicionais sobre figuras de rosto utilizadas na públicação


import xml.etree.ElementTree as ET

# Caminho do arquivo XML
file_path = "Patente_2828_18032025.xml"

# Parse do arquivo XML
tree = ET.parse(file_path)
root = tree.getroot()

# Dicionário para armazenar os INID encontrados
inid_dict = {}

# Busca por atributos e elementos com "inid"
for elem in root.iter():
    inid = elem.attrib.get("inid")
    if inid:
        inid_dict[inid] = elem.tag  # Armazena o nome da tag associada ao INID

# Ordena os INID encontrados
inid_dict = dict(sorted(inid_dict.items()))

# Retorna a lista dos INID encontrados e suas respectivas tags
print(inid_dict)

for despacho in root.findall('./despacho'):
    if despacho.find("titulo").text == "Extinção - Art. 86 da LPI":
        print(despacho.find("titulo").text)