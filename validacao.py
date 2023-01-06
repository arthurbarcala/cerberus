import pandas as pd #importando pandas para lidar com os dados
from cerberus import Validator #lib para validação dos dados (pip|pip3 install cerberus)

#lendo o arquivo csv, criando dataframe
df = pd.read_csv('./pokemon_data.csv')
df.head() #lê as primeiras linhas

#print(df.columns)

#schema => dict com o nome de cada coluna e atribuindo um tipo específico
schema = {
    '#':{'type':'number'},
    'Name':{'type':'string'},
    'Type 1':{'type':'string'},
    #Type 2 pode ser string ou NaN
    'HP':{'type':'number'},
    'Attack':{'type':'number'},
    'Defense':{'type':'number'},
    'Sp. Atk':{'type':'number'},
    'Sp. Def':{'type':'number'},
    'Speed':{'type':'number'},
    'Generation':{'type':'number'},
    'Legendary':{'type':'boolean'},
}

#fazendo a validação
v = Validator(schema)
v.allow_unknown = True
v.require_all = True
# print(v.validate({'Name':'Bulbasaur'})) #verifica se as informações inseridas como param estão na tabela, se sim retorna true, se não retorna false
# print(v.errors)

df_dict = df.to_dict(orient='records')
df_dict[:2]

#for que repete e valida, se n validar mostra erros
for index, record in enumerate(df_dict):
    if not v.validate(record):
        print(f"Item {index} : {v.errors}")
