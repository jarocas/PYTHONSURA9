from curses.ascii import TAB
import pandas as pd

tablaempleados=pd.read_csv('./empleados.csv')

#print(tablaempleados)
#print(tablaempleados.to_string())

#filtro 1 quiero obtener todos los datos de los analistas 1
tablaempleados1=tablaempleados[tablaempleados["cargo"]=="analista1"].head(50)
archivoHTML=tablaempleados1.to_html()

archivoTEXTO=open("datosanalistas1.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()