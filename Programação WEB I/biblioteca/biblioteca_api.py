# Importa as ferramentas necessárias do Flask e da biblioteca padrão de XML
from flask import Flask, request, jsonify, Response
import xml.etree.ElementTree as ET


app = Flask(__name__)


livros = [
    {
        "id": 1,
        "titulo": "O Guia do Mochileiro das Galáxias",
        "autor": "Douglas Adams",
        "ano": 1979
    },
    {
        "id": 2,
        "titulo": "1984",
        "autor": "George Orwell",
        "ano": 1949
    }
]


@app.route("/livros", methods=["GET"])
def listar_livros():
    
    if request.headers.get("Accept") == "application/xml":
        
        root_xml = ET.Element("livros")
        for livro in livros:
            livro_xml = ET.SubElement(root_xml, "livro") 
            
            ET.SubElement(livro_xml, "id").text = str(livro['id'])
            ET.SubElement(livro_xml, "titulo").text = livro['titulo']
            ET.SubElement(livro_xml, "autor").text = livro['autor']
            ET.SubElement(livro_xml, "ano").text = str(livro['ano'])
        
        
        xml_string = ET.tostring(root_xml, encoding="unicode")
        
        return Response(xml_string, mimetype="application/xml")
    
    
    return jsonify(livros)


@app.route("/livros", methods=["POST"])
def adicionar_livro():
    
    novo_livro = request.json
    
    livros.append(novo_livro)
   
    return jsonify({
        "mensagem": "Livro adicionado com sucesso!",
        "livro": novo_livro
    }), 201


if __name__ == "__main__":
    app.run(debug=True)