import xml.etree.ElementTree as ET

# Créer la racine de l'arbre XML
root = ET.Element("person")
name = ET.SubElement(root, "name")
name.text = "John Doe"

age = ET.SubElement(root, "age")
age.text = "30"

# Convertir l'arbre en chaîne XML
xml_string = ET.tostring(root, encoding='utf8').decode('utf8')

print(xml_string)
