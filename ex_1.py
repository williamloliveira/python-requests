import requests

VIACEP_URI = 'http://viacep.com.br/ws/06020190/json/'

response = requests.get(VIACEP_URI)

print('Status Code', response.status_code)
print('Texto Plano',response.text)
print('Dicionario do Python',response.json())