import pandas as pd

dados = pd.read_excel("lista.xlsx")
print(dados.head())
print("==========================================================")

# usando loc
# por linhas
print(dados.loc[2])
print("**********************************************************")
print(dados.loc[1:5])
print("**********************************************************")
print(dados.loc[::2])
print("**********************************************************")
print(dados.loc[2:7, ["NOME", "IDADE"]])
print("**********************************************************")
print(dados.loc[2:7, "NOME":"PROFISSAO"])
print("**********************************************************")
print(dados.loc[[1, 3, 4]])
print("##########################################################")

# usando iloc
# não inclui o 6 do intervalo, somente o itervalo entre o 2 e o 6
print(dados.iloc[2:6])
print("**********************************************************")
print(dados.iloc[2:6, 1:3])
print("==========================================================")

