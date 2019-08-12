import pandas as pd

# caminho absoluto ou relativo do csv, encoding do csv, a separação dentro do arquivo, pegando
# do arquivo csv
df = pd.read_csv("dados.csv", encoding="UTF-8", sep=";", header=0) 
print(df.head())
print("============================================================================================")

# Selecionando algumas colunas
df = pd.read_csv("dados.csv", encoding="UTF-8", sep=";", usecols=["AddressID", "AddressLine1"]) 
print(df.head())
print("============================================================================================")

#Selecionando algumas linhas
df = pd.read_csv("dados.csv", encoding="UTF-8", sep=";", usecols=["AddressID", "AddressLine1"], nrows=200) 
print(df.head())
print("============================================================================================")