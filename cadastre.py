import os
import json
import pandas as pd 

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def choose_file(files):
    print("Veuillez choisir un fichier:")
    for i, file in enumerate(files):
        print(f"{i + 1}. {file}")
    choice = int(input("Entrez le numéro du fichier: ")) - 1
    return files[choice]

directory = 'parcelles'
files = list_files(directory)
chosen_file = choose_file(files)
print(f"Vous avez choisi le fichier: {chosen_file}")

surface = int(input("Entrez la surface de la parcelle: "))
print(f"surface choisie: {surface}m²")

file_path = os.path.join(directory, chosen_file)
print(f"Chemin du fichier: {file_path}")

with open(file_path, 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)

print(df.head())