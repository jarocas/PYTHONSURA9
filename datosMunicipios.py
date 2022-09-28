import pandas as pd

tablaMunicipios=pd.read_csv('./Siembras.csv')

#filtar los datos de los municipios(andes, barbosa, caldas, tamesis y yarumal)

tablamunicipios1=tablaMunicipios[(tablaMunicipios["Ciudad"]=="Andes") | (tablaMunicipios["Ciudad"]=="Barbosa") | (tablaMunicipios["Ciudad"]=="Caldas") | (tablaMunicipios["Ciudad"]=="Tamesis") | (tablaMunicipios["Ciudad"]=="Yarumal")]
#print(tablamunicipios1.to_string())

archivoHTML=tablamunicipios1.to_html()
archivoTEXTO=open("datosMunicipio.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()