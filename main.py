import json
import requests
import urllib
import random

from dotenv import dotenv_values

# Importar `username` e `password` do arquivo .env
try:
    config = dotenv_values()
    username = config['USERNAME']
    password = config['PASSWORD']
except KeyError:
    print("\nArquivo .env não encontrado ou incompleto. Por favor, crie um arquivo com o nome '.env' e certifique-se que contém as seguintes linhas linhas:")
    print("USERNAME=seu_nome_de_usuario")
    print("PASSWORD=sua_senha\n")


user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'


data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']

images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]

arquivoDados = open("dados.json")
dados = json.load(arquivoDados)
arquivoDados.close()

inicios = dados["inicios"]
meios = dados["meios"]
fins = dados["fins"]

memes_2_textos = dados["memes_2_textos"]
memes_3_textos = dados["memes_3_textos"]

id = random.randint(1, 101)

text1 = random.choice(inicios)
text2 = random.choice(meios)
text3 = random.choice(fins)

URL = 'https://api.imgflip.com/caption_image'
params = {
    'username':username,
    'password':password,
    'template_id':images[id-1]['id'],
    'text0':(text1 + text2),
    'text1':text3
}
response = requests.request('POST',URL,params=params).json()
print(response)

opener = urllib.request.URLopener()
opener.addheader('User-Agent', user_agent)
filename, headers = opener.retrieve(response['data']['url'], images[id-1]['name']+str(random.randint(1,100000))+'.jpg')
