from fastapi import FastAPI, HTTPException
import httpx
import os

app = FastAPI()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "api-football-v1.p.rapidapi.com"

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST
}

@app.get("/")
def root():
    return {"status": "API de predicción de goles en vivo activa 🚀"}

@app.get("/teams")
async def get_teams(league_id: int = 39, season: int = 2023):
    url = f"https://{RAPIDAPI_HOST}/v3/teams"
    params = {"league": league_id, "season": season}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error al obtener datos")

    return response.json()
