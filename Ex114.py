import requests

try:
    site = requests.get('http://www.pudim.com.br')
    print('\033[33mConsegui acessar o site Pudim com sucesso!\033[m')
except:
    print('\033[31mERRO! Não foi possível acessar o site\033[m')
