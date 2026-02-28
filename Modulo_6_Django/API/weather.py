# https://www.weatherapi.com/
# importa a biblioteca requests (pip install requests)
import requests
import pprint

# chave de acesso
api_key = "7ecfc760bcad488f93f21445262302"
# link da api
api_link = "http://api.weatherapi.com/v1/current.json"

# parametros
parametros = {
    "key": api_key,
    "q": "Salvador",
    "lang": "pt"
}
# buscando os dados de acordo com os parametros passados
response = requests.get(api_link, params=parametros)
# print(response.status_code)
# print(response.content)
# se a resposta for ok
if response.status_code == 200:
    # gera os dados json
    dados = response.json()
# se existir dados
if dados:
    # printa em formato amigavel
    # pprint.pprint(dados)
    # coleta os dados
    temperatura = dados["current"]["temp_c"]
    Indice_UV = dados["current"]["uv"]
    condicao = dados["current"]["condition"]["text"]
    # pronta os dados
    print(f"Temperatura atual: {temperatura}")
    print(f"Indice_UV: {Indice_UV}")
    print(f"Condição do tempo: {condicao}")
else:
    # informe erro
    print("Falha ao recuperar dados")
