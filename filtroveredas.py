import pandas as pd

tablaVeredas=pd.read_csv('./Siembras.csv')

tablaVeredasRS=tablaVeredas[(tablaVeredas["Vereda"]=="Rio Arriba") | (tablaVeredas["Vereda"]=="La Salazar")]
#print(tablaVeredasRS)

archivoHTML=tablaVeredasRS.to_html()
archivoTEXTO=open("RioArribaLaSalazar.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()