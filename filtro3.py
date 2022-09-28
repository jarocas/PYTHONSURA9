import pandas as pd

tablaCaucasia=pd.read_csv('./Siembras.csv')

tablaCaucasia1=tablaCaucasia[(tablaCaucasia["Ciudad"]=="Caucasia")]
tablaCaucasia2=tablaCaucasia1["Hectareas"].to_frame()
#print(tablaCaucasia2.to_string())

archivoHTML=tablaCaucasia2.to_html()
archivoTEXTO=open("CaucasiaHectareas.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()