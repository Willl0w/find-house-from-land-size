import os
import json
import pandas as pd 

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def choose_file(files):
    while True:
        try:
            print("\n📁 Veuillez choisir un fichier:")
            for i, file in enumerate(files):
                print(f"  {i + 1}. 📄 {file}")
            choice = int(input("🔍 Entrez le numéro du fichier: ")) - 1
            
            if 0 <= choice < len(files):
                return files[choice]
            else:
                print("❌ Erreur: Numéro de fichier invalide")
        except ValueError:
            print("❌ Erreur: Veuillez entrer un nombre valide")


def get_valid_surface():
    while True:
        try:
            surface = int(input("\n📏 Entrez la surface de la parcelle: "))
            return surface
        except ValueError:
            print("❌ Erreur: Veuillez entrer un nombre entier valide")


directory = 'parcelles'
files = list_files(directory)
chosen_file = choose_file(files)
print(f"\n✅ Vous avez choisi le fichier: {chosen_file}")

surface = get_valid_surface()
print(f"📐 Surface choisie: {surface}m²")

file_path = os.path.join(directory, chosen_file)
print(f"📍 Chemin du fichier: {file_path}")

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame([feature['properties'] for feature in data['features']])

print("\n📋 Colonnes disponibles:")
print("-"*50)
print(df.columns)
print("-"*50)

filtered_df = df[df['contenance'] == surface]

if filtered_df.empty:
    print(f"\n❌ Aucune parcelle trouvée avec une surface de {surface}m²")
    print("\n🔍 Recherche des parcelles similaires...")
    
    # Recherche dans une plage de +/- 10m²
    similar_df = df[
        (df['contenance'] >= surface - 10) & 
        (df['contenance'] <= surface + 10)
    ]
    
    if similar_df.empty:
        print("❌ Aucune parcelle trouvée dans un rayon de ±10m²")
    else:
        print(f"\n✨ Parcelles trouvées entre {surface-10}m² et {surface+10}m²:")
        print("="*50)
        result_df = similar_df.sort_values('contenance')[['section', 'numero', 'contenance']]
        print(result_df.to_string(index=False))
        print("="*50)
else:
    print(f"\n🎯 Parcelles trouvées avec une surface de {surface}m²:")
    print("="*50)
    result_df = filtered_df.reset_index()[['index', 'section', 'numero']]
    print(result_df.to_string(index=False))
    print("="*50)