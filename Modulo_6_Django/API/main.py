# importa a biblioteca requests (pip install requests)
import requests

# metodo para consumir uma API


def fetch_data(endpoint):
    # criando uma requisicao que consume uma api
    response = requests.get(f"https://rickandmortyapi.com/api/{endpoint}")

    # se a resposta for ok
    if response.status_code == 200:
        # recupera os dados no formato json
        return response.json()
    else:
        # retorna vazio
        return None


# passando o dado para a api
dados = fetch_data("character")
# se existrem dados
if dados:
    # imprima
    print(dados)
else:
    # informe erro
    print("Falha ao recuperar dados")
