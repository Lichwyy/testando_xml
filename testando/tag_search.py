import xml.etree.ElementTree as ET


tree = ET.parse('Patente_2828_18032025.xml')
root = tree.getroot()

tags_list = list()

for tag in root.iter():
    if tag.tag not in tags_list:
        tags_list.append(tag.tag)
    
print(tags_list)