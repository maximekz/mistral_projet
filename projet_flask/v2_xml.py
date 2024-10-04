from flask import Flask, Response
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def display_xml():
    # Créer la racine de l'arbre XML
    root = ET.Element("person")
    name = ET.SubElement(root, "name")
    name.text = "John Doe"

    age = ET.SubElement(root, "age")
    age.text = "300"

    # Convertir l'arbre en chaîne XML
    xml_string = ET.tostring(root, encoding='utf8').decode('utf8')

    # Retourner l'XML dans une réponse HTTP avec le type MIME correct
    return Response(xml_string, mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True)
