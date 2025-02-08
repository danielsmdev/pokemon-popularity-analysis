import pandas as pd

# Función para guardar datos parciales cada N Pokémon
def save_partial_data(df, count, folder_path="../data/partial_data"):
    file_name = f"{folder_path}/pokemon_partial_{count}.csv"
    df.to_csv(file_name, index=False)
    print(f"📁 Guardado parcial en '{file_name}'")

# Función para filtrar Pokémon con variantes sin cambios en estadísticas ni habilidades
def filter_pokemon_variants(df):
    duplicated_pokemon = df[df.duplicated(subset=["index"], keep=False)]

    stats_cols = ["hp", "attack", "defense", "sp_atk", "sp_def", "speed"]
    filtered_pokemon = []

    for _, group in duplicated_pokemon.groupby("index"):
        base_form = group.iloc[0]  
        unique_forms = group.drop_duplicates(subset=stats_cols + ["abilities", "hidden_ability"])

        if len(unique_forms) > 1:
            filtered_pokemon.append(unique_forms)
        else:
            filtered_pokemon.append(base_form.to_frame().T)

    df_filtered = pd.concat(filtered_pokemon)
    df_final = pd.concat([df[~df["index"].isin(duplicated_pokemon["index"])], df_filtered])
    
    # Ordenar por índice y mantener la forma base primero
    df_final.sort_values(by=["index", "variant"], ascending=[True, False], inplace=True)
    
    return df_final