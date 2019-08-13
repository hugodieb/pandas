import pandas as pd

# carrega os dados da planilha excel
dados = pd.read_excel("lista.xlsx")
print(dados.head())
print("======================================================")

# pega o dado de uma coluna 
print(dados["NOME"].head())
print("======================================================")

# pega dado de varias colunas
print(dados[["ID","NOME", "PROFISSAO"]].head())
print("======================================================")

# tambem funciona
print(dados.NOME.head())
print("======================================================")