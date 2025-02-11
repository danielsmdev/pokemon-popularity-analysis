import requests
import pandas as pd
import time

def get_base_name(pokemon_name):
    """Elimina progresivamente los sufijos después de '-' hasta encontrar un nombre válido en la API."""
    parts = pokemon_name.split("-")
    
    while parts:
        base_name = "-".join(parts)
        url = f"https://pokeapi.co/api/v2/pokemon-species/{base_name.lower()}"
        response = requests.get(url)

        if response.status_code == 200:
            return base_name  # ✅ Devolvemos el nombre en cuanto sea válido
        
        parts.pop()  # Eliminamos el último sufijo e intentamos de nuevo

    return pokemon_name  # ❌ Si no se encontró ningún válido, devolvemos el original con advertencia


def clean_pokemon_name(pokemon_name):
    """ Extrae el nombre base del Pokémon y su variante. """
    return pokemon_name.split("-", 1)[0], pokemon_name.split("-", 1)[1] if "-" in pokemon_name else None

# Obtener la lista de nombres desde la PokeAPI
def get_pokemon_names():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1025"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [pokemon["name"] for pokemon in data["results"]]
    print("❌ Error al obtener la lista de nombres de Pokémon")
    return []

# Obtener todas las formas de un Pokémon
# 📌 Función para obtener todas las formas de un Pokémon, intentando con el nombre completo y luego con el base
def get_all_forms(pokemon_name):
    """
    Intenta obtener todas las formas de un Pokémon.
    - Primero intenta con el nombre original.
    - Si falla, prueba eliminando sufijos hasta encontrar el nombre base válido.
    """
    url_full = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}"
    response = requests.get(url_full)

    if response.status_code == 200:
        data = response.json()
        varieties = [var["pokemon"]["name"] for var in data["varieties"]]
        return varieties

    # Si falla con el nombre completo, reducir progresivamente los sufijos
    base_name = get_base_name(pokemon_name)

    if base_name != pokemon_name:  # Solo intentar si el nombre cambió
        url_base = f"https://pokeapi.co/api/v2/pokemon-species/{base_name.lower()}"
        response = requests.get(url_base)

        if response.status_code == 200:
            data = response.json()
            varieties = [var["pokemon"]["name"] for var in data["varieties"]]
            return varieties

    print(f"⚠️ No se encontraron formas para {pokemon_name} ni {base_name}")
    return [pokemon_name]

# Obtener datos del Pokémon
def get_pokemon_data(pokemon_name, base_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Obtener datos básicos
        name = data["name"]
        types = " / ".join([t["type"]["name"] for t in data["types"]])
        height = data["height"] / 10  
        weight = data["weight"] / 10  

        # Extraer habilidades separando normales y ocultas
        normal_abilities = []
        hidden_ability = None  

        for ability in data["abilities"]:
            ability_name = ability["ability"]["name"]
            if ability["is_hidden"]:
                hidden_ability = ability_name  # Solo una habilidad oculta
            else:
                normal_abilities.append(ability_name)

        normal_abilities = " / ".join(normal_abilities)

        # Obtener estadísticas base
        stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
        hp = stats.get("hp", 0)
        attack = stats.get("attack", 0)
        defense = stats.get("defense", 0)
        sp_atk = stats.get("special-attack", 0)
        sp_def = stats.get("special-defense", 0)
        speed = stats.get("speed", 0)

        # Separar nombre base y variante
        base_name, variant = (name.split("-", 1) + [None])[:2]
        full_name = f"{base_name}-{variant}" if variant else base_name

        print(f"✅ {full_name} (Base: {base_name}, Variante: {variant}) -> {types}, HP: {hp}, Speed: {speed}")

        return {
            "index": base_id,
            "name": full_name,
            "type": types,
            "height": height,
            "weight": weight,
            "abilities": normal_abilities,
            "hidden_ability": hidden_ability,
            "hp": hp,
            "attack": attack,
            "defense": defense,
            "sp_atk": sp_atk,
            "sp_def": sp_def,
            "speed": speed
        }

    print(f"❌ Error al obtener {pokemon_name} (Código: {response.status_code})")
    return None  # Devuelve None explícitamente para detección de errores




def get_species_data(pokemon_name):
    base_name, _ = clean_pokemon_name(pokemon_name)  # Extraer nombre base
    print(f"🔍 Intentando obtener especie de: {pokemon_name} (Base: {base_name})")  # Debug

    urls = [
        f"https://pokeapi.co/api/v2/pokemon-species/{base_name.lower()}",
        f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}"
    ]

    for url in urls:
        print(f"🌐 Consultando API en: {url}")  # Ver qué URL se consulta
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            is_legendary = data["is_legendary"]
            is_mythical = data["is_mythical"]
            generation = data["generation"]["name"]

            print(f"✅ Especie encontrada para {pokemon_name}: Legendario: {is_legendary}, Mítico: {is_mythical}, Generación: {generation}")

            return {"legendary": is_legendary, "mythical": is_mythical, "generation": generation}

    print(f"❌ Error al obtener especie de {pokemon_name} (Intentado con: {base_name})")
    return {"legendary": None, "mythical": None, "generation": None}
