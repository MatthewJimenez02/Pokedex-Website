from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_pokemon_data(name_or_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{name_or_id.lower()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "name": data['name'].title(),
            "id": data['id'],
            "height": data['height'],
            "weight": data['weight'],
            "types": [t['type']['name'] for t in data['types']],
            "abilities": [a['ability']['name'] for a in data['abilities']],
            "stats": {stat['stat']['name']: stat['base_stat'] for stat in data['stats']},
            "sprite": data['sprites']['other']['official-artwork']['front_default']
        }
    except:
        return None

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, pokemon: str = None):
    poke_data = get_pokemon_data(pokemon) if pokemon else None
    return templates.TemplateResponse("index.html", {"request": request, "data": poke_data})
