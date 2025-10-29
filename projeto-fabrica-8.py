from flask import Flask, jsonify, request

app = Flask(__name__)

playlist = [{
  "id": 1, "titulo": "Astronomia", "artista": "Tony Igy", "duracao": 236, "url": "https://example.com/tony-igy-astronomia"}
]

@app.route("/tracks", methods=["GET"])
def get_tracks():
    return jsonify({"playlist": playlist, "total": len(playlist)}), 200

@app.route("/tracks/<int:id>", methods=["GET"])
def get_track_by_id(id):
  for musica in playlist:
    if musica["id"] == id:
      return jsonify({"mensagem": "Música encontrada!", "musica": musica})

  return jsonify({"mensagem": "Música não enontrada!"}), 404

@app.route("/tracks", methods=["POST"])
def add_track():
  nova_musica = request.json

  nova_musica["id"] = len(playlist) + 1

  playlist.append(nova_musica)
  return jsonify({"mensagem": "Música adicionada!", "musica": nova_musica})

@app.route("/tracks/<int:id>", methods=["PUT"])
def update_track(id):
  dados = request.json

  for musica in playlist:
    if musica["id"] == id:
      musica.update(dados)
      return jsonify({"mensagem": "Música atualizade!"})

  return jsonify({"Erro": "Música não encotrada!"}), 404

@app.route("/tracks/<int:id>", methods={"DELETE"})
def delete_track(id):
  for musica in playlist:
    if musica["id"] == id:
      playlist.remove(musica)
      return jsonify({"mensagem": "Música apagada!"}), 200
    
    return jsonify({"Erro": "Música não encotrada!"}), 404