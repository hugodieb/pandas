import pandas as pd

# Ler um arquivo excel
df = pd.read_excel("dados.xlsx")
print(df.head())
print("============================================================================================")

# Posso usar o nome da aba da planilha ou o indice
df = pd.read_excel("dados.xlsx", sheet_name="Aba2")
print(df.head())
print("============================================================================================")

# Exibir nome das abas em forma de lita
files_excel = pd.ExcelFile("dados.xlsx")
print(files_excel.sheet_names)
print("============================================================================================")

# Usando parse
aba1 = files_excel.parse(files_excel.sheet_names[0])
aba2 = files_excel.parse(files_excel.sheet_names[1])
print(aba1.head())
print("********************************************************************************************")
print(aba2.head())
print("============================================================================================")