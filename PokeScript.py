import requests

def get_pokemon_data(name_or_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{name_or_id.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Pokémon not found!")
        return

    data = response.json()
    
    print(f"\nName: {data['name'].title()}")
    print(f"ID: {data['id']}")
    print(f"Height: {data['height']}")
    print(f"Weight: {data['weight']}")
    print("Types:", ', '.join(t['type']['name'] for t in data['types']))
    print("Abilities:", ', '.join(a['ability']['name'] for a in data['abilities']))
    print("Stats:")
    for stat in data['stats']:
        print(f"  {stat['stat']['name']}: {stat['base_stat']}")
    print("\n")

if __name__ == "__main__":
    while True:
        user_input = input("Enter Pokémon name or ID (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        get_pokemon_data(user_input)
