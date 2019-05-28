import requests

API_URI = 'https://gen-net.herokuapp.com/api/users'

response = requests.get(API_URI)

users = response.json()

#for u in users:
#        print('Usuario',users)

user_id = None

caduser = {
    'name': input('Digite seu nome: '),
    'email': input('Digite seu email: '),
    'password': input('Digite sua senha: ')
    }

r = requests.post(API_URI, json=caduser)

if r.status_code == 200:
    print('Cadastro concluido com sucesso!')
    user_id = r.json()['id']
    print('Id do usuario cadastrado: ', user_id)
elif r.status_code == 404:
    print('Not Found.')

API_URI = 'https://gen-net.herokuapp.com/api/users/{}'.format(user_id)

r = requests.get(API_URI)

print('User',r.json())
