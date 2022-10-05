#Los datos de la veredas Quitasol de BELLO ordenados de menor a mayor y el promedio de arboles sembrados en esta vereda
import pandas as pd

tablaBelloQuitasol=pd.read_csv('./Siembras.csv')

DatosBelloQuitasol=tablaBelloQuitasol[tablaBelloQuitasol["Ciudad"]=="Bello"]
DatosBelloQuitasol2=DatosBelloQuitasol[DatosBelloQuitasol["Vereda"]=="Quitasol"].sort_values("Arboles",ascending=True)
tablaEstadisticas=DatosBelloQuitasol2.describe()
promedios=tablaEstadisticas.loc[['mean']]
promedioArboles=promedios["Arboles"].to_frame()

#print(promedioArboles)


'''archivoHTML=DatosBelloQuitasol2.to_html()
archivoTEXTO=open("BelloQuitasol.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()'''

archivoHTML=promedioArboles.to_html()
archivoTEXTO=open("promedioArbolesBS.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()