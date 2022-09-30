import pandas as pd

tablaSantafedeAntioquia=pd.read_csv('./Siembras.csv')

tablaSantafedeAntioquia1=tablaSantafedeAntioquia[(tablaSantafedeAntioquia["Ciudad"]=="Santa Fe de Antioquia") & (tablaSantafedeAntioquia["Arboles"]>250)]
#print(tablaSantafedeAntioquia1)

archivoHTML=tablaSantafedeAntioquia1.to_html()
archivoTEXTO=open("SantafedeAntioquia.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()