import os
import json
jsonfile= "usuarios.json"

def load_dados():
    if os.path.exists(jsonfile):
        with open(jsonfile, "r") as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return {}
    return {}

def save_dados(dados):
    with open(jsonfile, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)