import pandas as pd

#lendo os arquivos csv, excel e txt (como csv)
data = pd.read_csv('pokemon_data.csv')

data_xlsx = pd.read_excel('pokemon_data.xlsx')

data_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')

#imprimindo dados 
""" print(data.head(3)) 

print(data.columns)

print(data['Name']) """

print(f"Quantidade de colunas: {len(data_xlsx.columns)}")
#for x in data_xlsx.columns:
    #print(f"{x} = {data_xlsx.columns[0].index(x)}")
print(data_xlsx.column)
