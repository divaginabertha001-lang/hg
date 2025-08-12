from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from ytmusicapi import YTMusic
from typing import Optional
import uvicorn

app = FastAPI()

# Permitir CORS para o Netlify
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode trocar para o domínio do seu Netlify se quiser restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa API do YouTube Music (modo anônimo)
ytmusic = YTMusic()

# ==============================
# Rotas que o frontend espera
# ==============================

@app.get("/api/youtube/search")
def search_youtube(q: str = Query(..., description="Termo de busca")):
    results = ytmusic.search(q, filter="songs")
    return {"results": results}

@app.get("/api/youtube/playlists/search")
def search_playlists(q: str = Query(..., description="Busca playlists")):
    results = ytmusic.search(q, filter="playlists")
    return {"results": results}

@app.get("/api/youtube/playlists/{playlist_id}")
def get_playlist_details(playlist_id: str):
    playlist = ytmusic.get_playlist(playlist_id, limit=100)
    return playlist

@app.get("/api/playlists/{playlist_id}")
def get_playlist(playlist_id: str):
    playlist = ytmusic.get_playlist(playlist_id, limit=100)
    return playlist

@app.get("/api/playlists/{playlist_id}/tracks")
def get_playlist_tracks(playlist_id: str):
    playlist = ytmusic.get_playlist(playlist_id, limit=100)
    return {"tracks": playlist.get("tracks", [])}

# ==============================
# Início local
# ==============================
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
