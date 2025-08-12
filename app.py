from flask import Flask, request, jsonify
from flask_cors import CORS
from ytmusicapi import YTMusic

app = Flask(__name__)
CORS(app)  # Libera CORS para qualquer origem (para seu Netlify conseguir acessar)

# Inicializa o YTMusic (usando sem autenticação, modo público)
ytmusic = YTMusic()

@app.route("/search")
def search():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "Missing 'query' parameter"}), 400
    results = ytmusic.search(query)
    return jsonify(results)

@app.route("/song")
def song():
    song_id = request.args.get("id")
    if not song_id:
        return jsonify({"error": "Missing 'id' parameter"}), 400
    details = ytmusic.get_song(song_id)
    return jsonify(details)

@app.route("/playlist")
def playlist():
    playlist_id = request.args.get("id")
    if not playlist_id:
        return jsonify({"error": "Missing 'id' parameter"}), 400
    details = ytmusic.get_playlist(playlist_id)
    return jsonify(details)

@app.route("/")
def home():
    return jsonify({"status": "ytmusicapi backend is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
