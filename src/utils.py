import os
import json

def from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def initialize_user_json(caminho_arquivo):
  diretorio = os.path.dirname(caminho_arquivo)
  if not os.path.exists(diretorio):
    os.makedirs(diretorio)

  if not os.path.isfile(caminho_arquivo):
    with open(caminho_arquivo, 'w') as f:
      json.dump({"fase" : 0, "score" : 0}, f)

