import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/GiomarMC/MILLIONAIRE_PROJECT/main/Numeros_Ganadores.csv")
df = df[['NG 1','NG 2','NG 3','NG4 ','NG 5','NG 6']]
df.columns = ['NG_1','NG_2','NG_3','NG_4','NG_5','NG_6']
print(df)
orden = pd.DataFrame()
orden['Numeros'] = range(1,47)
for i in df.columns:
    lista = []
    for j in orden.Numeros:
        try:
            lista.append(df[i].value_counts()[j])
        except KeyError:
            lista.append(0)
    orden[i] = lista
print(orden)
orden.to_excel("Frecuencia_NumerosG.xlsx")
orden.to_csv("Frecuencia_NumerosG.csv")