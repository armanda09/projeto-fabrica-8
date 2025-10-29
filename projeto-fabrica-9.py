from flask import Flask, jsonify, request

app = Flask(__name__)

itens = [
    {"id": 1, "nome": "Arroz 5kg", "quantidade": 2, "categoria": "Alimentos", "prioridade": "alta", "comprado": False}
    {"id": 1, "nome": "Feijão 1kg", "quantidade": 10, "categoria": "Alimentos", "prioridade": "alta", "comprado": False}
]

@app.route("/itens", methods=["GET"])
def get_items():
    return jsonify({"itens": itens, "total": len(itens)})

@app.route("/items/<int:id>", methods=["GET"])
def get_item_by_id(id):
    for item in itens:
        if item["id"] == id:
            return jsonify({"mensagem": "Item encontrado!", "item": item})

    return jsonify({"erro": "Item não encontrado!"}), 404

@app.route("/items", methods=["POST"])
def add_item():
    novo_item = request.json

    novo_item["id"] = len(itens) + 1

    itens.append(novo_item)
    return jsonify({"mensagem": "Item cadastrado!", "item": novo_item})

@app.route("/items/<int:id>", methods=["PUT"])
def update_item(id):
    dados = request.json

    for item in itens:
        if item["id"] == id:
            item.update(dados)
            return jsonify({"mensagem": "Item atualizado!"})
    
    return jsonify({"erro": "Item não encontrado"}), 404

@app.route("/items/<int:id>", methods=["DELETE"])
def delete_item(id):
    for item in itens:
        if item["id"] == id:
            itens.remove(item)
            return jsonify({"mensagem": "Item deletado!"})

    return jsonify({"erro": "Item não encontrado!"}), 404