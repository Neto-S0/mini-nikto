import requests

def scan_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException:
        return None





# importa a biblioteca requests

# cria uma função scan_url(url)

# tenta:
#     fazer uma requisição HTTP para a URL (com limite de 5 segundos)
#     se funcionar:
#         retorna o código HTTP do site

# se der erro (conexão, timeout, etc):
#     não trava o programa
#     retorna None

# ------------------------- #

# # Importa a biblioteca requests (usada para fazer requisições HTTP)
# import requests

# # Cria uma função chamada scan_url que recebe uma URL como parâmetro
# def scan_url(url):
    
#     # Tenta executar o código abaixo
#     try:
#         # Faz uma requisição HTTP para a URL (com limite de 5 segundos)
#         response = requests.get(url, timeout=5)
        
#         # Se funcionar, retorna o código HTTP do site (ex: 200, 404, 403)
#         return response.status_code
    
#     # Se der erro (conexão, timeout, etc)
#     except requests.exceptions.RequestException:
        
#         # Não trava o programa, apenas retorna None
#         return None