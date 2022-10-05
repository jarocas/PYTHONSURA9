import pandas as pd

tablaCaramanta=pd.read_csv('./Siembras.csv')

#filtar los datos de los municipios(andes, barbosa, caldas, tamesis y yarumal)

DatosCaramanta=tablaCaramanta[(tablaCaramanta["Ciudad"]=="Caramanta")]
#print(DatosCaramanta)

archivoHTML=DatosCaramanta.to_html()
archivoTEXTO=open("datosCaramanta.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()